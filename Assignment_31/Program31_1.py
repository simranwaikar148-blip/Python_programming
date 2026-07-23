# Display a predefined message repeatedly after a specified interval.

import schedule
import time

MESSAGE = "Jay Ganesh"
INTERVAL = 5

def display_message():
    print(MESSAGE)

def main():

    if INTERVAL <= 0:
        print("Interval must be greater than zero.")
        return

    schedule.every(INTERVAL).seconds.do(display_message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()