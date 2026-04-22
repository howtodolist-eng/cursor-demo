bill_amount = float(input("Enter the bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

tip_amount = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip_amount

print(f"\nTip amount: ${tip_amount:.2f}")
print(f"Total bill: ${total_bill:.2f}")
