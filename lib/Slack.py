# -*- coding: utf-8 -*-

import requests

class Slack:

	apiBaseUrl = "https://slack.com/api";

	def __init__(self, token):
		self.token = token

	def postMessage(self, params):
		url = self.apiBaseUrl + "/chat.postMessage"
		params["token"] = self.token
		requests.session().post(url, data=params)
