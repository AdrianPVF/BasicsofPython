# Write your code here :-)
# Get the total, average, and final rating for two outputs
# Terminates when the condition for score is false
# Repeats for preceding input


def AddNum(num1, num2):
    total = num1 + num2
    return total


def Average(num1, num2):
    avg = (num1 + num2) / 2
    return avg


def Calculate_rating(num1, num2):
    rating = ((num1 + num2) / 2) / 0.5
    return rating


while True:

    num1 = int(input("Enter first score: "))

    if num1 <= 50:
        print("Score is valid")
    else:
        print("Error! Score is invalid")
        break

    num2 = int(input("Enter second score: "))

    if num2 <= 50:
        print("Score is valid")
    else:
        print("Error! Score is invalid")
        break

    print("Total:", AddNum(num1, num2))

    print("Average:", Average(num1, num2))

    print("Grade:", Calculate_rating(num1, num2), "%")

    if Calculate_rating(num1, num2) >= 80:
        print("You passed!")
    elif Calculate_rating(num1, num2) < 80:
        print("You failed!")

# Loop using while
