#!/bin/sh

/usr/sbin/telnetd -F -p 4123 -l /bin/sh &
/usr/local/bin/python -u /ping.py
