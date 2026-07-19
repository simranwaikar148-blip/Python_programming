#Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

def display_contents(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
            
    except FileNotFoundError:
        print("File not found.")


def main():
    filename = input("Enter file name: ")
    display_contents(filename)


if __name__ == "__main__":
    main()