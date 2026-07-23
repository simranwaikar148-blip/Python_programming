#Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

import os

def main():
  

    if(os.path.exists("Demo.txt")):
        print("File is present in current directory")
    else:
        print("There is no such file")


if __name__ =="__main__":
    main()