#Write a program which accepts a name from the user and displays the length of the name.

def NameLength(name):
    return(len(name))


def main():
    name = input("Enter name: ")

    result =  NameLength(name)
    print("Length of name: ",result)
   
    

if __name__ == "__main__":
    main()