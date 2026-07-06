#Write a program which accepts N numbers from the user and stores them into a list. Return the maximum number from that list.

def Maximum(arr):
    max_no = arr[0]

    for i in arr:
        if i > max_no:
            max_no = i

    return max_no
    

def main():
    size = int(input("Enter number of elements: "))

    data = []

    print("Enter elements:")
    for i in range(size):
        value = int(input())
        data.append(value)

    result = Maximum(data)

    print("Maximum number :",result)


if __name__ == "__main__":
    main()