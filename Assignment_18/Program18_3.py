#Write a program which accepts N numbers from the user and stores them into a list. Return the minimum number from that list.

def Minimum(arr):
    min_no = arr[0]

    for i in arr:
        if i < min_no:
            min_no = i

    return min_no


def main():
    size = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(size):
        value = int(input())
        data.append(value)

    result = Minimum(data)

    print("Minimum number =", result)


if __name__ == "__main__":
    main()