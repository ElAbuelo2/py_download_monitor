#!/usr/bin/env python

## Based on original Download Monitor v0.1 - March 2012
##     Source: http://askubuntu.com/questions/105536/tool-to-shutdown-system-when-there-is-no-network-traffic
##     Hacked by me to include auto interface listing and other goodies

# Note for Python 3: getoutput won't work, it was moved to subprocess module.
# I will rewrite this script for proper Python 3 compatibility but for now
# adapt to your needs.

# Set the minimum download speed in KB/s that must be achieved.
MINIMUM_SPEED = 6

# Set the number of retries to test for the average minimum speed. If the average speed is less
# than the minimum speed for x number of retries, then shutdown.
RETRIES = 120 # 20 minutes (120 retries with 10 seconds sleep)

# Set the interval (in seconds), between retries to test for the minimum speed.
INTERVAL = 10

import os, time
from commands import getoutput
from list_interfaces import list_interfaces

if __name__ == "__main__":
	RETRIES_COUNT = RETRIES
	while True:
		ifs = list_interfaces()
		speed = 0.0
		for inter in ifs:
			if inter[0] == "lo": # ignore lo
				continue
			speed = float(getoutput("ifstat -i %s 1 1 | awk '{print $1}' | sed -n '3p'" % inter[0]))
			if speed >= MINIMUM_SPEED:
				break
		if (speed < MINIMUM_SPEED and RETRIES_COUNT <= 0):
			os.system("shutdown -h now")
		elif speed < MINIMUM_SPEED:
			RETRIES_COUNT -= 1
			time.sleep(INTERVAL)
		else:
			RETRIES_COUNT = RETRIES
			time.sleep(INTERVAL)
