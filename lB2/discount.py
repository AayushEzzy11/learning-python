
purchase_amount = float(input("Enter the purchase amount: $"))


if purchase_amount > 10000:
    discount = 0.20  
    print("You get a 20% discount!")
elif purchase_amount >= 5000:
    discount = 0.10  
    print("You get a 10% discount!")
else:
    discount = 0 
    print("No discount applicable")


discount_amount = purchase_amount * discount
final_price = purchase_amount - discount_amount


print(f"\nPurchase Amount: ${purchase_amount:.2f}")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")
