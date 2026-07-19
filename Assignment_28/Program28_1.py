#Write a program which accepts a file name from the user and counts how many lines are present in the file.

def count_lines(filename):
    try:
        with open(filename, "r") as file:
            count = 0
            for line in file:
                count += 1
            print("Total number of lines:",count)

    except FileNotFoundError:
        print("File not found")


def main():
    filename = input("Enter file name: ")
    count_lines(filename)


if __name__ == "__main__":
    main()