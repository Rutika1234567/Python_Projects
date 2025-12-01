menu = {
    "pizza": 40,
    "burger": 60,
    "coffee": 40,
    "salad": 70,
    "pasta": 50
}

print("Welcome to PYTHON restaurant.\n")
print("Menu:")
print(" Pizza: Rs40\n Burger: Rs60\n Coffee: Rs40\n Salad: Rs70\n Pasta: Rs50\n")

order_total = 0
order_details = []  # Added to store bill items

while True:
    item = input("Enter the name of the item you want to order: ").lower()

    if item in menu:
        qty = int(input(f"How many {item} do you want? : "))
        price = menu[item] * qty
        order_total += price
        print(f"{qty} {item}(s) added to your order.\n")

        # Saving details for bill 
        order_details.append([item.capitalize(), qty, menu[item], price])

    else:
        print(f"Ordered item '{item}' is not available.\n")

    another = input("Do you want to order another item? (yes/no): ").lower()
    if another != "yes":
        break
#printing bill 

print("\n" + "="*40)
print("             PYTHON RESTAURANT BILL")
print("="*40)
print(f"{'Item':<15}{'Qty':<5}{'Price':<8}{'Total'}")
print("-"*40)

for item, qty, unit_price, total in order_details:
    print(f"{item:<15}{qty:<5}{unit_price:<8}{total}")


print(f"{'Grand Total':<28} Rs {order_total}")
print("="*40)
print("Thank you for ordering with us!")

