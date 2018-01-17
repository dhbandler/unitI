#Daniel 
#1/17/18
#age.py asks for first and last name and age
name=input("What is your name? ")
name1, name2= name.split()
let=len(name1)
print("your first name has", let, "letters")
nom=len(name2)
print("your last name has", nom, "letters")
age=int(input("how old are you?"))
print("You are", age+1, "years old next year")