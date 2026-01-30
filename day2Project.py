print("Welcome to the tip calculator")
bill = int(input("please enter a bill amount"))
tip = int(input("please enter % tip you want to give "))

final_bill = (bill + (bill*(tip/100)))
print(final_bill)
number_of_buddies = int(input("enter no of people to divide a bill"))
perheadamount = final_bill / number_of_buddies
print(f"The main bill will be {bill} and the amount of bill after tip will be {final_bill} and per head amount need to pay {perheadamount}")