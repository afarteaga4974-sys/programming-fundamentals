#Code by Andersson 1-B
#exercise:fuel cost
#get data

liters = float(input("Enter the number of liters: "))
price = float(input("enter the price per liter: "))

#calculate total cost
total = liters * price

#aply discount
if liters >50:
    discount = total * 0.05
    total = total - discount

#display final cost
print("total cost to pay:" , round(total,2))
