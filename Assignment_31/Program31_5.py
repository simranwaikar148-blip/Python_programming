# Count the number of files in a directory every 5 minutes.
# Store details in DirectoryCountLog.txt.

import schedule
import time
import os
from datetime import datetime

DIRECTORY = "Sample"

def count_files():

    if not os.path.exists(DIRECTORY):
        print("Directory does not exist.")
        return

    count = 0

    for item in os.listdir(DIRECTORY):
        if os.path.isfile(os.path.join(DIRECTORY, item)):
            count += 1

    with open("DirectoryCountLog.txt", "a") as log:
        log.write("Directory: " + DIRECTORY + "\n")
        log.write("Number of Files: " + str(count) + "\n")
        log.write("Date & Time: " +
                  datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
        log.write("\n\n")

    print("Log updated successfully.")

def main():

    schedule.every(5).minutes.do(count_files)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()