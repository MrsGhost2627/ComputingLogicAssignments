
# --------------------------------------------
# Create a list containing 15 numbers
# --------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# --------------------------------------------
# For loop to process each number in the list
# --------------------------------------------
for number in numbers:
    # Check if the number is even using modulo operator
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
        
