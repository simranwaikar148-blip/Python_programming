# Delete all empty files from a specified directory every hour.
# Scan recursively and store deleted file paths in a log file.

import schedule
import time
import os
from datetime import datetime

DIRECTORY = "Sample"

def delete_empty_files():

    log = open("DeletedFilesLog.txt", "a")

    for root, dirs, files in os.walk(DIRECTORY):

        for file in files:

            filepath = os.path.join(root, file)

            try:
                if os.path.getsize(filepath) == 0:
                    os.remove(filepath)

                    log.write(filepath + " deleted at " +
                              datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

                    print(filepath, "deleted.")

            except PermissionError:
                print("Permission denied:", filepath)

            except Exception:
                print("Error:", filepath)

    log.close()

def main():
    schedule.every(1).hours.do(delete_empty_files)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()