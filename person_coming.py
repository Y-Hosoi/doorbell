#!/user/bin/python
# coding: utf-8

import grovepi
import slackweb
slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

# Connecct the Grove Light Sensorto analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

grovepi.pinMode(light_sensor,"INPUT")

while True:
    try:
         # Get sensor value
         sensor_value = grovepi.analogRead(light_sensor)

         if sensor_value > 700:
            #sent to slack
            import datetime
            import time
            t = datetime.datetime.now()
            d = t + datetime.timedelta(hours=9)
            slack.notify(text="Person Comes " + d.strftime("%H:%M"))
            print ("Person Comes")
            time.sleep(15)

         else:
            pass

    except IOError:
        print ("Error")
