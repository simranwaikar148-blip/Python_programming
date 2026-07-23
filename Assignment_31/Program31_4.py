# Create a new log file every 10 minutes.
# Filename should contain current date and time.

import schedule
import time
from datetime import datetime

def create_log():

    now = datetime.now()

    filename = "MarvellousLog_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(filename, "w") as file:
        file.write("Log file created successfully.\n")
        file.write("Creation Time: " +
                   now.strftime("%d-%m-%Y %I:%M:%S %p"))

    print(filename, "created.")

def main():

    schedule.every(10).minutes.do(create_log)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()