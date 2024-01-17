
fruit_prices = {'Apple': 2, 'Grape': 1, 'Orange': 3}


name = input("Welcome to the GC Fruit Market!\nWhat is your name?\n> ")
fruit_counts = {fruit: 0 for fruit in fruit_prices}

while True:
    print(f"\nWelcome {name}. Which Fruit would you like to buy?")
    for i, (fruit, price) in enumerate(fruit_prices.items(), start=1):
        print(f"{i}. {fruit} ${price}")

    selected_option = int(input("> "))
    selected_fruit = list(fruit_prices.keys())[selected_option - 1]


    fruit_counts[selected_fruit] += 1


    response = input(
        f"You bought 1 {selected_fruit} at ${fruit_prices[selected_fruit]}\nWould you like to buy another piece of fruit? Enter 'yes' for yes, 'no' for no\n> ")


    if response.lower() != 'yes':
        break


subtotal = sum(fruit_counts[fruit] * fruit_prices[fruit] for fruit in fruit_counts)


tax_rate = 0.05
tax = subtotal * tax_rate


total = subtotal + tax


print(f"\nOrder for {name}:")
for fruit, count in fruit_counts.items():
    if count > 0:
        print(f"{count} {fruit}(s) at ${fruit_prices[fruit]} apiece")

print(f"\nSub Total: ${subtotal:.2f}")
print(f"5% Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")





