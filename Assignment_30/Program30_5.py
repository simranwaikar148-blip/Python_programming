# Schedule a task that executes every five minutes.
# Append the current date and time to Marvellous.txt.

import schedule
import time
from datetime import datetime

def write_file():
    now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("Marvellous.txt", "a") as file:
        file.write("Task executed at: " + now + "\n")

    print("Task executed and written to Marvellous.txt")

def main():
    schedule.every(5).minutes.do(write_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()