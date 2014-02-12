#coding:utf-8

from tools import time2deg


class City:
	def __init__(self, coordinates, timeOffset):
		self.latitude, self.longitude = [time2deg(x) for x in coordinates]
		self.timeOffset = timeOffset
