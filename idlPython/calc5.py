#calc2
#import packages
import os
from random import randint
#initialize, no mandatory, except constant or accountants
os.system("clear")
print("hello.loading basic Calc..")
#get data (inputs)
num1=randint(-100,100)
num2=randint(-100,100)
#display generated numbers
print("number1 is: ",num1)
print(f"number2 is: {num2}")#manera mas formal de hacer las cosas
#display Main menu
print("Main menu")
print("[1].Addition\n[2].Substraction\n[3].Multiplication\n[4].Division\n[5].Alloperations")
opt=int(input("please,press any option[1-5]: "))
match opt:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)
    case 5:
        print(num1+num2)
        print(num1-num2)
        print(num1*num2)
        print(num1/num2)
    case _:
        print("error")

    
                   
              
