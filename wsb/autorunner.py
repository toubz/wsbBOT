#!/usr/bin/python

import schedule
import time
import subprocess

def job():
    subprocess.call("py .\wsbtickerbot.py")


schedule.every().monday.at("09:00").do(job)
schedule.every().tuesday.at("09:00").do(job)
schedule.every().wednesday.at("09:00").do(job)
schedule.every().thursday.at("09:00").do(job)
schedule.every().friday.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)