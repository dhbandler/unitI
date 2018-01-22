#Daniel
#1/17/18
#tip.py, calculates tip for meal

price=float(input("How much did your meal cost?   "))

tip=float(input("What is the decimal value of your tip?"))
if tip<.1:
    print("You are going to have to do better than that, you dumb cheapskate")

    
else:
    print("Your tip is", price*tip, "dollars")
    print("Thank you for coming here")
    
