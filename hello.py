def calculate_total ():
    return 100

print(calculate_total()) # 100  

def calculate_total_with_tax(total, tax_rate):
    return total * (1 + tax_rate)

print(calculate_total_with_tax(100, 0.05)) # 105

def calculate_total_with_discount(total, discount_rate):
    return total * (1 - discount_rate)

print(calculate_total_with_discount(100, 0.1))  # 90                