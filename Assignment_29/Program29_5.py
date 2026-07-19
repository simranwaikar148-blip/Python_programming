#Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

def string_frequency(filename, word):
    try:
        with open(filename, "r") as file:
            text = file.read()

        count = text.count(word)
        print(f'"{word}" appears {count} time(s) in the file.')

    except FileNotFoundError:
        print("File not found.")


def main():
    filename = input("Enter file name: ")
    word = input("Enter string to search: ")
    string_frequency(filename, word)


if __name__ == "__main__":
    main()