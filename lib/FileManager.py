# -*- coding: utf-8 -*-

import os.path

class FileManager:

	@staticmethod
	def touch(path):
		f = open(path, "a")
		os.chmod(path, 0o664)
		f.close()

	@staticmethod
	def write(path, data):
		f = open(path, "w")
		content = f.write(data)
		f.close()

	@staticmethod
	def read(path):
		if os.path.exists(path):
			f = open(path, "r")
			data = f.read()
			f.close()
			return data
		else:
			return None
