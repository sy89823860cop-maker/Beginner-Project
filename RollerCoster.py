print("Welcome to the rollercoaster ride! ")
Name = input("Please Enter your name : ")
height=int(input("Please enter you height in cm : "))
bill = 0
if height>=120:
    age=int(input(f"Hello {Name} Please enter your age : "))
    if age <= 12:
        print("For Child  5$")
        bill = 5
    elif age <=18:
        print("Since you are Teenager 10$")
        bill =10
    else :
        print(f"Since you are Adults {Name}! You have to pay 15$")
        bill = 15
    #add photos for 3$
    photos=(input(f"Do you want photos {Name }? Type y for yes and n for no :")).lower()
    if photos== "y":
        bill +=3
        print("Photos added = 3$:")
        print(f"You have to pay {bill}$")

        print("Thank you for your time!")
    else :
        print("Thank you for your time!")
else :
     print("Sorry you cannot have ride this time ")