# -*- coding: utf-8 -*-

import json
import os.path

from Config import *
from FileManager import FileManager
from Slack import Slack
from Teacher import Teacher

data_dir = os.path.dirname(os.path.abspath(__file__)) + "/../data"

if not os.path.exists(data_dir):
	os.mkdir(data_dir)

if not os.path.exists(data_dir + "/schedules.json"):
	FileManager.touch(data_dir + "/schedules.json")
	FileManager.write(data_dir + "/schedules.json", json.dumps([]))

teacher = Teacher(teachers)

(schedules, updatedTeachers) = ([], [])
for t in teachers:
	previousAvailableTimes = teacher.getPreviousAvailableTimes(t["id"])
	availableTimes = teacher.getAvailableTimes(t["id"])

	isUpdated = not set(availableTimes).issubset(set(previousAvailableTimes))
	if (isUpdated):
		updatedTeachers.append(t)

	schedules.append({
		"teacher_id" : t["id"],
		"available_times" : availableTimes,
	})

if updatedTeachers:
	slack = Slack(slackAccessToken)

	for t in updatedTeachers:
		msg = t["name"] + "'s lessons have been updated.\n"
		msg += teacher.baseUrl + "/teacher/index/" + str(t["id"])

		slack.postMessage({
			"channel" : slackChannel,
			"username" : "update",
			"text" : msg,
		})

FileManager.write(data_dir + "/schedules.json", json.dumps(schedules))
