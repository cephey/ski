#coding:utf-8
from datetime import timedelta
from math import radians, degrees


def deg2rad(deg):
	return radians(deg)


def deg2time(deg):
	result = list()
	rem = deg
	for d in [1, 60, 60]:
		resFrac = d * rem
		resInt = int(resFrac)
		rem = round(resFrac - resInt, 4)
		result.append(resInt)
	return result


def rad2deg(rad):
	return degrees(rad)


def rad2time(rad):
	return deg2time(rad2deg(rad))


def time2deg(timeDeg):
	res = 0
	for t, d in zip(timeDeg, [1, 60, 3600]):
		res += t / d
	return round(res, 4)


def time2rad(timeDeg):
	return deg2rad(time2deg(timeDeg))


def time2timeD(angTime):
	d, h = divmod(angTime[0], 24)
	m, s = angTime[1:]
	return timedelta(d, seconds=h * 3600 + m * 60 + s)


def deg2timeD(deg):
	return time2timeD(deg2time(deg))


def rad2timeD(rad):
	return time2timeD(rad2time(rad))


def chSign(value):
	return -value if value > 0 else abs(value)


def iterPair(iterable):
	for i in range(1, len(iterable)):
		yield iterable[i - 1], iterable[i]
