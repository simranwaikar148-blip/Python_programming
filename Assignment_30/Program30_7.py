# Write a Python program that performs a file backup every hour.
# Copy a predefined source file to a destination folder.
# Add current date and time to the backup filename.
# Store backup details in backup_log.txt.

import schedule
import time
import shutil
import os
from datetime import datetime

# Predefined paths (Modify according to your system)
SOURCE_FILE = "sample.txt"
DESTINATION_FOLDER = "Backup"

def backup_file():
    if not os.path.exists(DESTINATION_FOLDER):
        os.makedirs(DESTINATION_FOLDER)

    filename = os.path.basename(SOURCE_FILE)
    name, extension = os.path.splitext(filename)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    backup_name = name + "_" + timestamp + extension

    destination = os.path.join(DESTINATION_FOLDER, backup_name)

    shutil.copy2(SOURCE_FILE, destination)

    log_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    with open("backup_log.txt", "a") as log:
        log.write("Backup completed successfully at " + log_time + "\n")

    print("Backup completed successfully.")

def main():
    schedule.every(1).hours.do(backup_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()