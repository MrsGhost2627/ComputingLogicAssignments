# Program: Raining Cats and Dogs
# Author: Thaija Wilson
# Description:
#   This program demonstrates variable assignment and string concatenation.
#   It prints the sentence: "It is raining cats and dogs."
#   Variables:
#       c → holds the string "cats."
#       d → holds the string "dogs."
#       s → holds the full sentence to be printed

def main():
    # Variable assignments
    c = "cats."       # String variable for cats
    d = "dogs."       # String variable for dogs

    # Construct the sentence using variables
    s = "It is raining " + c + " and " + d

    # Output the sentence
    print(s)

# Program execution starts here
if __name__ == "__main__":
    main()
