#Write a program which accepts N numbers from the user and stores them into a list. Return the addition of all prime numbers from that list. Create a user-defined module named MarvellousNum containing the function ChkPrime(). The main file should call ListPrime().

def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True