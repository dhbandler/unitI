#Daniel
#1/24/18
#change.py takes in amound of money and outputs necessary smaller denomination

val=float(input("Input the number in cents that you have"))

quart=val//25
rem1=val % 25

dim = rem1//10
rem2 = rem1 % 10

nick =  rem2//5
rem3 = rem2 % 5

pen = rem3//1


print("You have ", quart, " quarters")
print("You have ", dim, " dimes")
print("You have ", nick, " nickles")
print("You have ", pen, " pennies")

