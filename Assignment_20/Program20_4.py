# Create three threads Small, Capital and Digits.
# Count lowercase letters, uppercase letters and digits.

import threading

def Small(text):
    count = sum(1 for ch in text if ch.islower())
    print("\nThread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Lowercase Count:", count)

def Capital(text):
    count = sum(1 for ch in text if ch.isupper())
    print("\nThread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Uppercase Count:", count)

def Digits(text):
    count = sum(1 for ch in text if ch.isdigit())
    print("\nThread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digit Count:", count)

def main():
    text = input("Enter a string: ")

    t1 = threading.Thread(target=Small, args=(text,), name="Small")
    t2 = threading.Thread(target=Capital, args=(text,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(text,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()