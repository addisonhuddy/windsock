# Windsock

Simple python script designed to emulate thousands of IoT connected windsocks pinging information to a central system.

Included in the message
* Device id
* Wind direction
* Wind speed

Deploy to cloud foundry with `cf push windsock`.

Start command `python windsock.py [threads] [server] [port]`
