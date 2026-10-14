#ticket discount

amount = float(input("enter the purchase amount: "))

if amount > 100:
    discount = amount * 0.15
    total = amount - discount
else:
        total = amount 
  
print("final amount to pay: ", round(total,2))
