#lambda function using filter() to return strings having length greater than 5

def main():
   words = input("Enter words: ").split()

   result = filter(lambda x: len(x) > 5,words)

   print("Strings with length greater than 5:",result)

if __name__ == "__main__":
   main()