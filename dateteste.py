#!/usr/bin/python3

#https://pypi.org/project/isoweek/

from isoweek import Week

w = Week(2018, 45)
#print("Week %s starts on %s" % (w, w.monday()))
print("Week %s starts on %s" % (w, w.monday().strftime('%Y%m%d')))
#print("Current week number is", Week.thisweek().week)
#print("Next week is", Week.thisweek() + 1)