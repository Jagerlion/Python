import random

def main():
    """Inputs the bounds of the range of numbers,
    and lets the user guess the computer's number until
    the guess is correct."""
    low = int(input("Enter the smaller number: "))
    high = int(input("Enter the larger number: "))
    myNumber = random.randint(low, high)
    count = 0
    while True:
        count += 1
        userNumber = int(input("Enter your guess: "))
        if userNumber < myNumber:
            print("Too small")
        elif userNumber > myNumber:
            print("Too large")
        else:
            print("You've got it in", count, "tries!")
            break

if __name__ == "__main__":
    main()