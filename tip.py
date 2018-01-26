#Daniel
#1/17/18
#tip.py, calculates tip for meal

price=float(input("How much did your meal cost?   "))

tip=float(input("What is the decimal value of your tip? "))
if tip<.1:
    print("Only a", price*tip, "dollar tip? You are going to have to do better than that, you stingy reprobate")
    
else:
    print("Your tip is", price*tip, "dollars")
    print("Thank you for coming here")
    
