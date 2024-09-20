def calculate_discount(price,discount_percent):

    if discount_percent >= 20:
        return (price*discount_percent)/100
    else:
        return price
price = int(input("Original Price:"))
discount_percent = float(input("Enter the discount percentage: "))
    
print(calculate_discount(price,discount_percent))    