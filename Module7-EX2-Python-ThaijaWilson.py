def main():
    coffee_price = 2.00
    total_price = coffee_price

    addins = {
        "Whipped cream": 0.89,
        "Cinnamon": 0.25,
        "Chocolate sauce": 0.59,
        "Amaretto": 1.50,
        "Irish whiskey": 1.75
    }

    print("Enter add-ins (type 'done' to finish):")

    while True:
        item = input("Add-in: ")
        if item.lower() == "done":
            break
        elif item in addins:
            print(f"Price: ${addins[item]:.2f}")
            total_price += addins[item]
        else:
            print("Sorry, we do not carry that.")

    print(f"\nTotal price: ${total_price:.2f}")

if __name__ == "__main__":
    main()
