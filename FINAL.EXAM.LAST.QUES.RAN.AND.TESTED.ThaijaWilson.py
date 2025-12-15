# Drop the four lowest scores on the ten 100-point quizzes

SIZE = 10
MAX = 6   # number of highest scores to keep

scores = []
total = 0

def fillArray():
    for x in range(SIZE):
        score = int(input(f"Enter quiz score {x + 1}: "))
        scores.append(score)

def sortArray():
    # Ascending bubble sort (lowest scores first)
    for x in range(SIZE - 1):
        for y in range(SIZE - x - 1):
            if scores[y] > scores[y + 1]:
                scores[y], scores[y + 1] = scores[y + 1], scores[y]

def displayTotal(name):
    total = 0
    # Add only the six highest scores
    for x in range(SIZE - 1, SIZE - MAX - 1, -1):
        total += scores[x]

    print("\nStudent Name:", name)
    print("Total points for top six quizzes:", total)

# ---------- Main Program ----------
name = input("Enter student name: ")

fillArray()
sortArray()
displayTotal(name)
