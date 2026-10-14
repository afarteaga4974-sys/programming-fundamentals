#code by Andersson Felipe Arteaga Yaluzan
#login acces

#get predefinied data

correct_username = "admin"
correct_password = "1234"

#get inputs
username = input("enter your username: ")
password = input("enter your password: ")

if username==correct_username and password == correct_password:
    print("acces granted")
else:
        print("acces denied")
