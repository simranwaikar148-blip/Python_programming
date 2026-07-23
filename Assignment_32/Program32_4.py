# Copy all .txt files from one directory to another every 10 minutes.
# Maintain a log file.

import schedule
import time
import os
import shutil
from datetime import datetime

SOURCE_DIR = "Source"
DEST_DIR = "Destination"

def copy_files():

    if not os.path.exists(SOURCE_DIR):
        print("Source directory does not exist.")
        return

    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    log = open("CopyLog.txt", "a")

    for file in os.listdir(SOURCE_DIR):

        if file.endswith(".txt"):

            source = os.path.join(SOURCE_DIR, file)
            destination = os.path.join(DEST_DIR, file)

            try:
                shutil.copy2(source, destination)

                log.write(file + " copied at " +
                          datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

                print(file, "copied.")

            except Exception:
                log.write("Failed to copy " + file + "\n")

    log.close()

def main():
    schedule.every(10).minutes.do(copy_files)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()