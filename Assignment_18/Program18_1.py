#Write a program which accepts N numbers from the user and stores them into a list. Return the addition of all elements from that list.

def SumList(arr):
    total = 0

    for i in arr:
        total += i

    return total


def main():
    size = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(size):
        value = int(input())
        data.append(value)

    result = SumList(data)

    print("Addition :",result)


if __name__ == "__main__":
    main()