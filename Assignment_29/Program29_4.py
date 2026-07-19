#Write a program which accepts two file names through command line arguments and compares the contents of both files.

#If both files contain the same contents, display Success.
#Otherwise display Failure.

import sys

def compare_files(file1, file2):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            if f1.read() == f2.read():
                print("Success")
            else:
                print("Failure")
    except FileNotFoundError:
        print("One or both files not found.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <file1> <file2>")
        return

    compare_files(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()