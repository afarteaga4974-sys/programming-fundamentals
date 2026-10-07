#calc2
#import packages
import os
from random import randint
#initialize, no mandatory, except constant or accountants
num1=0
num2=0
add=0
subs=0
mult=0
div=0
opt=0
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
#print(opt==1)
if opt==1:
    add=num1+num2
    print(f"addition is: {add}")
if opt==2:
    subs=num1-num2
    print(f"substraction is: {subs}")
if opt==3:
    mult=num1*num2
    print(f"multiplication is: {mult}")
if opt==4:
    div=num1/num2
    print(f"divition is: {div}")
if opt==5:
        add=num1+num2
        subs=num1-num2
        mult=num1*num2
        div=num1/num2
        print(f"addition is: {add}\nsubstraction is {subs}\nmultiplication is: {mult}\ndivition is: {div}")
if opt <1 or opt >5:
    print("invalid option.Try again")
