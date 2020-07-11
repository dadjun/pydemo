#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar
import time

def testTIme():
    ticks = time.time()
    print(ticks)
    localtime = time.localtime(time.time())
    print(time.localtime())
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(time.asctime(localtime))
    print(time.timezone / 3600)

def printcurTime():
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    return
def printCalendar():
    cal = calendar.month(2020,1)
    print(cal)
