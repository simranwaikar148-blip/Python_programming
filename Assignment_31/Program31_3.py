# Scan a specified directory every minute and display:
# Directory name, number of files,
# number of subdirectories and scan time.

import schedule
import time
import os
from datetime import datetime

DIRECTORY = "Sample"

def scan_directory():

    if not os.path.exists(DIRECTORY):
        print("Directory does not exist.")
        return

    files = 0
    folders = 0

    for item in os.listdir(DIRECTORY):
        path = os.path.join(DIRECTORY, item)

        if os.path.isfile(path):
            files += 1
        elif os.path.isdir(path):
            folders += 1

    print("Directory:", DIRECTORY)
    print("Total Files:", files)
    print("Total Subdirectories:", folders)
    print("Scan Time:", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print()

def main():

    schedule.every(1).minutes.do(scan_directory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()