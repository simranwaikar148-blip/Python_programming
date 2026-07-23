# Write a program that creates a new text file every minute.
# The filename should contain the current timestamp.
# Write filename, creation date and creation time into the file.

import schedule
import time
from datetime import datetime

def create_file():
    now = datetime.now()

    filename = "File_" + now.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(filename, "w") as file:
        file.write("Filename : " + filename + "\n")
        file.write("Creation Date : " + now.strftime("%d-%m-%Y") + "\n")
        file.write("Creation Time : " + now.strftime("%I:%M:%S %p") + "\n")

    print(filename, "created successfully.")

def main():
    schedule.every(1).minutes.do(create_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()