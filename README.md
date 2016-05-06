# Windsock

Simple python apps designed to emulate thousands of IoT connected windsocks pinging information to a central system.


## Generator

Included in the message
* Device id
* Wind direction
* Wind speed

Within the generator directory, deploy to cloud foundry with `cf push windsock`.
Start command `python windsock.py [threads] [server] [port]`

## Dashboard

Within the generator directory, deploy to cloud foundry with `cf push windsock-dashboard`.

Uses gemfire backend and communicates via REST.

Device specific average windspeed from last two minutes
`/gemfire-api/v1/windsock/device/<device_id>`

Global windspeed on earth
`/gemfire-api/v1/windsock/global`
