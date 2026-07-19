#Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.

import sys

def copy_file(source):
    try:
        with open(source, "r") as file1:
            data = file1.read()

        with open("Demo.txt", "w") as file2:
            file2.write(data)

        print("Contents copied successfully to Demo.txt.")
    except FileNotFoundError:
        print("Source file not found.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <source_file>")
        return

    copy_file(sys.argv[1])


if __name__ == "__main__":
    main()