#Daniel
#1/24/18
#change.py takes in amound of money and outputs necessary smaller denomination

val=float(input("Input the number in cents that you have"))

quart=val//25
rem1=val % 25

dim=rem1//10
rem2=rem1 % 10
print("You have", quart, "quarters")
print(dim)

