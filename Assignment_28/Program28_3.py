#Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

def display_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line,end=" ")

    except FileNotFoundError:
        print("File not found")


def main():
    filename = input("Enter filename: ")
    display_file(filename)



if __name__ == "__main__":
    main()