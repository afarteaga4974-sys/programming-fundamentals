#code created by Andersson 1B-M
#travel cost

#get number of days

days = int(input("enter number of days"))

#calculate cost
travelcost = days * 50
#aply discount
if days >7:
           discount = travelcost * 0.1
           travelcost = travelcost - discount
#display final cost
print("total travel's cost to pay:" , travelcost)
           
    

