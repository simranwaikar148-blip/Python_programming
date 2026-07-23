# Read and display the contents of a specified text file every minute.
# Handle:
# 1. File does not exist
# 2. File is empty
# 3. Permission denied
# 4. File cannot be opened

import schedule
import time

FILE_NAME = "sample.txt"

def read_file():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()

            if content.strip() == "":
                print("File is empty.")
            else:
                print("File Contents:")
                print(content)

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except Exception:
        print("File cannot be opened.")

def main():
    schedule.every(1).minutes.do(read_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()