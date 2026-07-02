#program to check whether a character is a vowel or consonant

def CheckVowel(ch):
    if ch.lower() in ['a','e','i','o','u']:
        print("Vowel")
    else:
        print("Consonant")


def main():
    ch = int(input("Enyer a character: "))
    CheckVowel(ch)

if __name__ == "__main__":
    main()