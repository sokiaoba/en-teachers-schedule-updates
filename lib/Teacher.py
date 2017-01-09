# -*- coding: utf-8 -*-

import json
import os.path
import phpserialize
import re
import urllib2

from FileManager import FileManager

class Teacher:

	baseUrl = "http://eikaiwa.dmm.com"

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
		html = urllib2.urlopen(self.baseUrl + "/teacher/index/" + str(teacherId)).read()
		tags = re.findall('<a.+?class="bt-open".*?>', html)

		availableTimes = []
		for tag in tags:
			_id = re.match('<a.+?id="(.+)".*>', tag).groups()[0]
			_id = _id.replace("&quot;", '"')
			availableTime = phpserialize.unserialize(_id)["launched"]
			availableTimes.append(availableTime)

		return availableTimes

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
