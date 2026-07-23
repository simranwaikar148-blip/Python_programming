#Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

def search_word(filename, word):
    try:
        with open(filename, "r") as file:
            text = file.read()

        if word in text:
            print(f'"{word}" is present in the file')
        else:
            print(f'"{word}" is not presnt in the file')

    except FileNotFoundError:
        print("File not found")

def main():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")
    search_word(filename, word )


if __name__ == "__main__":
    main()