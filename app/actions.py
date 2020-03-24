import time
from datetime import datetime, date, timedelta
from ..config import get_env

class Actions:
    def __init__(self, slackhelper, user_info=None):
        self.user_info = user_info
        self.slackhelper = slackhelper

    def notify_channel(self):
        while True:
            current_time = datetime.now()
            current_hour = current_time.hour
            current_minute = current_time.hour
            if current_hour - 8 > 0:
                sleep_time = 24 - current_hour + 8 - (current_minute/60)
            elif current_hour - 8 < 0:
                sleep_time = 8 - current_hour - (current_minute/60)
            elif current_hour == 8:
                if current_minute == 0:
                    sleep_time = 0
                else:
                    sleep_time = 24 - current_hour + 8 - (current_minute/60)
            time.sleep(sleep_time * 3600)

        