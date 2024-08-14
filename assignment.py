# Programmer: [Anierobi Eziolise]
# Course: CS701/GB-731, Dr. Yalew
# Date: [08/13/2024]
# Programming Assignment: 4
# Program Inputs: A positive integer < 1000
# Program Outputs: The English name of the integer

def main():
    # Prompt user for input
    number = int(input("Enter a positive integer less than 1000: "))
    
    # Validate the input
    if number < 1 or number >= 1000:
        print("The number must be between 1 and 999.")
        return

    # Convert the number to its English name and print it
    print(intName(number))

def digitName(digit):
    "Turns a digit into its English name."
    if digit == 1:
        return "one"
    elif digit == 2:
        return "two"
    elif digit == 3:
        return "three"
    elif digit == 4:
        return "four"
    elif digit == 5:
        return "five"
    elif digit == 6:
        return "six"
    elif digit == 7:
        return "seven"
    elif digit == 8:
        return "eight"
    elif digit == 9:
        return "nine"

def teenName(number):
    "Turns a number between 10 and 19 into its English name."
    if number == 10:
        return "ten"
    elif number == 11:
        return "eleven"
    elif number == 12:
        return "twelve"
    elif number == 13:
        return "thirteen"
    elif number == 14:
        return "fourteen"
    elif number == 15:
        return "fifteen"
    elif number == 16:
        return "sixteen"
    elif number == 17:
        return "seventeen"
    elif number == 18:
        return "eighteen"
    elif number == 19:
        return "nineteen"

def tensName(number):
    "Gives the name of the tens part of a number between 20 and 99."
    if number == 20:
        return "twenty"
    elif number == 30:
        return "thirty"
    elif number == 40:
        return "forty"
    elif number == 50:
        return "fifty"
    elif number == 60:
        return "sixty"
    elif number == 70:
        return "seventy"
    elif number == 80:
        return "eighty"
    elif number == 90:
        return "ninety"

def intName(number):
    "Turns a number into its English name."
    if number < 10:
        return digitName(number)
    elif 10 <= number < 20:
        return teenName(number)
    elif 20 <= number < 100:
        tens = number // 10 * 10
        ones = number % 10
        return tensName(tens) + ('' if ones == 0 else ' ' + digitName(ones))
    else:
        hundreds = number // 100
        remainder = number % 100
        return digitName(hundreds) + " hundred" + ('' if remainder == 0 else ' ' + intName(remainder))

# Start the program.
if __name__ == "__main__":
    main()
