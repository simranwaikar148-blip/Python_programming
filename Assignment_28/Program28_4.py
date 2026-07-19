#Write a program which accepts two file names from the user. The first file is an existing file and the second file is a new file. Copy all contents from the first file into the second file.

def copy_file(filename1, filename2):
    try: 
        with open(filename1, "r") as file1:
            data = file1.read()

        with open(filename2, "w") as file2:
            file2.write(data)

        print("Contents copied successfully")

    except FileNotFoundError:
        print("File not found")

def main():
    filename1 = input("Enter file name: ")
    filename2 = input("Enter file name: ")
    copy_file(filename1, filename2)
     


if __name__ == "__main__":
    main()