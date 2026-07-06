#Write a program which accepts N numbers from the user and stores them into a list. Accept one more number from the user and return the frequency of that number from the list.

def Frequency(arr, no):
    count = 0

    for i in arr:
        if i == no:
            count += 1

    return count


def main():
    size = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(size):
        value = int(input())
        data.append(value)

    search = int(input("Enter number to search: "))

    result = Frequency(data, search)

    print("Frequency =", result)


if __name__ == "__main__":
    main()