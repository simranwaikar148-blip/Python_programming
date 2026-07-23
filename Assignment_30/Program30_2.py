# Write a Python program that displays the current date and time after every one minute.

import schedule
import time
from datetime import datetime

def display_datetime():
    now = datetime.now()
    print("Current Date and Time:", now.strftime("%d-%m-%Y %I:%M:%S %p"))

def main():
    schedule.every(1).minutes.do(display_datetime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()