#code by Andersson Arteaga 
#temperature advice

#get temperature
temperature = float(input("enter temperature in celsius: "))

#check temperature range

if temperature <10:
    print("cold")
elif temperature <=25:
    print("comfortamble")
else:
    print("hot")
