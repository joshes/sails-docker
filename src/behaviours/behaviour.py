#!/usr/bin/env python
# This uses boatd_client, a python library for interacting with boatd. For more
# information, see https://github.com/boatd/python-boatd
# Run with $ python basic_behaviour.py, after boatd is running

from boatdclient import Boat

boat = Boat()

for i in range(5):
    boat.heading
    boat.wind
    boat.position
    boat.set_rudder(0)
    boat.set_rudder(-1)
    boat.set_rudder(3)
    boat.set_sail(0)
