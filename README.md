# py_download_monitor
Chek all your interfaces and shutdown system when no activity

No Windows/MAC support.

Inspired in a script shown for the first time at <http://askubuntu.com/questions/105536/tool-to-shutdown-system-when-there-is-no-network-traffic>
and adapted to check all interfaces.

Note that in modern Ubuntu versions command ifstat requires
installation. Use "sudo apt install ifstat". So if the script fails for
you this is the first thing to try.

Will fail in Python 3 due to API changes. Fix is easy and planned for
a near future. If you want to do this yourself, the getoutput function
was moved from command module to subprocess module, just change the
import.

At the time, most configurable variables are still hardcoded.

By default, the script requires 20 minutes with download below 6 KB/s to
shutdown the system. Some OS may require elevated privileges.

Modify global variable RETRIES to control this time.

Setting a sleep time too short is not recommended. The INTERVAL variable
controls this.

The lo interface is ignored, modify code if you want to include it. Turn
this on and off is planned for a future update.

Use CTRL+C to cancel if you changed your mind after running the script.

Set the executable bit and run with ./download_monitor.py or don't set
it and run with "python download_monitor.py".
