# Create a function DisplayMessage(message)
# and schedule it every 5 seconds.

import schedule
import time

MESSAGE = "Jay Ganesh"

def DisplayMessage(message):
    print(message)

def main():

    schedule.every(5).seconds.do(DisplayMessage, MESSAGE)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()