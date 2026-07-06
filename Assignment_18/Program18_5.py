import MarvellousNum

def ListPrime(arr):
    total = 0 

    for i in arr:
        if MarvellousNum.ChkPrime(i):
            total += i
    return total

def main():
    size = int(input("Enter number of elements: "))

    data = []

    print("Enter elements: ")
    for i in range(size):
        value = int(input())
        data.append(value)

    result = ListPrime(data)

    print("Addition of prime numbers: ",result)

if __name__ == "__main__":
    main()