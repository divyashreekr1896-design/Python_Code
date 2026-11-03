age=int(input("Enter the age"))#type casting
if age>=21:
    print("you are eligible for vote and participate in election")
elif age>=18 and age<21:
    print("Eligible for vote but not participation")
else:
    print("you are not elegible for both")