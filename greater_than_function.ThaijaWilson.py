
# ------------------------------------------------------
# Function Definition
# ------------------------------------------------------
def greater_than(x, y):
    """
    Returns True if x is greater than y.
    Otherwise returns False.
    """
    if x > y:
        return True
    else:
        return False

# ------------------------------------------------------
# Main Program
# ------------------------------------------------------

# Assign values to variables
a = 2
b = 3

# Call the function and store the result
result = greater_than(a, b)

# Print the formatted output
print(
    "The statement " 
    + str(a) 
    + " is greater than " 
    + str(b) 
    + " is " 
    + str(result)
)
