# Author: Jadon Argo
# Date: June 2025
# Assignment: Module 1 – 100 Bottles of Beer Countdown
# Description: This program asks the user for a number of bottles and
# counts down to 1 with custom lyrics. It ends with a reminder to buy more beer.

def beer_countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
        print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.\n")
    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")

def main():
    try:
        bottles = int(input("Enter number of bottles: "))
        if bottles <= 0:
            print("Please enter a positive number.")
            return
        beer_countdown(bottles)
        print("Go to the store and buy some more beer!")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

