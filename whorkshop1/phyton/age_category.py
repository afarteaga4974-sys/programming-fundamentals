#Code by Andersson 1-BM
#age_category

#get person's age

age = int(input("enter the person's age"))

#determine age category

if age < 0:
          print("invalid age")
elif age >=65:
    print("senior")
elif age >=18:
    print("adult")
elif age >=13:
    print("teenager")
else:
    print("child")
          

