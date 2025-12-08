def main():
    numbers = []
    sentinel = -1

    print("Enter up to 20 numbers (enter -1 to stop):")

    while len(numbers) < 20:
        num = int(input("Enter a number: "))
        if num == sentinel:
            break
        numbers.append(num)

    print("\nNumbers in reverse order:")
    for num in reversed(numbers):
        print(num)

if __name__ == "__main__":
    main()
