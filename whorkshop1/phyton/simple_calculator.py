#Code by Andersson Felipe 1B-M
#simple calculator
#get two numbers

numero1 = float(input("enter first number"))
numero2 = float(input("enter second number"))
operation = input("enter an operation (+, -, *, /): ")
if operation == "+" :
    print("result: " ,numero1 + numero2)
elif operation == "-" :
    print("result: " ,numero1 - numero2)
elif operation == "*" :
    print("result: " ,numero1 * numero2)
elif operation == "/" :
    if numero2 !=0:
        print("result: " , numero1 / numero2)
    else:
        print("error cannot divide by zero.")
else:
    print("error invalid opeeration")
