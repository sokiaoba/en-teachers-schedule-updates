# -*- coding: utf-8 -*-

import json
import os.path
import phpserialize
import re
import urllib2

from FileManager import FileManager

class Teacher:

	__teachers = None
	__previousSchedules = None
	__previousScheduleDict = None

	def __init__(self, teachers):
		self.__teachers = teachers

	def getPreviousAvailableTimes(self, teacherId):
		previousScheduleDict = self.__getPreviousScheduleDict()

		if teacherId in previousScheduleDict:
			return previousScheduleDict[teacherId]["available_times"]
		else:
			return []

	def getAvailableTimes(self, teacherId):
		try: 
			url = self.getIndexUrl(teacherId)
			req = urllib2.urlopen(url)
		except:
			return None

		if not req.geturl() == url:
			return None

		tags = re.findall('<a.+?class="bt-open".*?>', req.read())

		availableTimes = []
		for tag in tags:
			_id = re.match('<a.+?id="(.+)".*>', tag).groups()[0]
			_id = _id.replace("&quot;", '"')

			try:
				availableTime = phpserialize.unserialize(_id)["launched"]
			except:
				return None

			availableTimes.append(availableTime)

		return availableTimes

	def getIndexUrl(self, teacherId):
		return "http://eikaiwa.dmm.com/teacher/index/" + str(teacherId) + "/"

	def __getPreviousScheduleDict(self):
		def setSchedule(_dict, schedule):
			_dict[schedule["teacher_id"]] = schedule

		if self.__previousScheduleDict is None:
			_dict = {}
			map(lambda schedule: setSchedule(_dict, schedule), self.__getPreviousSchedules())
			self.__previousScheduleDict = _dict

		return self.__previousScheduleDict
	
	def __getPreviousSchedules(self):
		if self.__previousSchedules is None:
			data = FileManager.read(os.path.dirname(os.path.abspath(__file__)) + "/../data/schedules.json")
			if data is not None:
				self.__previousSchedules = json.loads(data)
			else:
				self.__previousSchedules = []

		return self.__previousSchedules
