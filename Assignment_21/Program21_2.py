# Create two threads to find the maximum and minimum elements from a list.

import threading

def Maximum(lst):
    print("Maximum Element:", max(lst))

def Minimum(lst):
    print("Minimum Element:", min(lst))

def main():
    n = int(input("Enter number of elements: "))
    lst = []

    print("Enter elements:")
    for i in range(n):
        lst.append(int(input()))

    t1 = threading.Thread(target=Maximum, args=(lst,))
    t2 = threading.Thread(target=Minimum, args=(lst,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()