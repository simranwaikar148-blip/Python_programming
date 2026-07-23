# Schedule two tasks:
# 1. Print Lunch Time! every day at 1:00 PM.
# 2. Print Wrap up work every day at 6:00 PM.

import schedule
import time

def lunch_time():
    print("Lunch Time!")

def wrap_up():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(lunch_time)
    schedule.every().day.at("18:00").do(wrap_up)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()