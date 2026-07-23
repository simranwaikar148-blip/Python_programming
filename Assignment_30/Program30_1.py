
# Write a Python program that prints "Jay Ganesh..." every two seconds.

import schedule
import time

def print_message():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(print_message)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()