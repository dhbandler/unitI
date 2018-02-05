#Daniel Bandler
#1/22/18
#slope.py calculate slope of given points

x1=float(input("Input the first x value here "))
y1=float(input("Input the first y value here "))

x2=float(input("Input the second x value here "))
y2=float(input("Input the second y value here "))


rise=(y2-y1)
run=(x2-x1)


if x1==x2:
    print("Slope is undefined, the equation is x=", x1)
else:
    print(rise/run)