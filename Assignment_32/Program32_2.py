# Monitor the size of a specified file every 30 seconds.
# Store details in FileSizeLog.txt.

import schedule
import time
import os
from datetime import datetime

FILE_PATH = "sample.txt"

def monitor_file():
    with open("FileSizeLog.txt", "a") as log:
        now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        if os.path.exists(FILE_PATH):
            size = os.path.getsize(FILE_PATH)

            log.write("File Path : " + FILE_PATH + "\n")
            log.write("File Size : " + str(size) + " bytes\n")
            log.write("Date & Time : " + now + "\n\n")

            print("File size recorded.")
        else:
            log.write("File not found : " + FILE_PATH + "\n")
            log.write("Date & Time : " + now + "\n\n")

            print("File does not exist.")

def main():
    schedule.every(30).seconds.do(monitor_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()