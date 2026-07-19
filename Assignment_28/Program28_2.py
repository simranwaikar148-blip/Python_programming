#Write a program which accepts a file name from the user and counts the total number of words in that file.

def count_words(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
            words = text.split()
        print("Total number of words: ",len(words))

    except FileNotFoundError:
        print("File not found")
         


def main():
    filename = input("Enter file name: ")
    count_words(filename)


if __name__ == "__main__":
    main()