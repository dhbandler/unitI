#Daniel
#1/19/18
#Slope.py Find the slope to a line

x1=float(input("Input first x value "))
y1=float(input("Input first y value "))
x2=float(input("Input second x value "))
y2=float(input("Input second y value "))

if x1==x2:
    print("The slope is undefined")
else:
    rise=(y2-y1)
    run=(x2-x1)
    slope=rise/run
    print("The slope is", slope)
    print("An equation for the line could be  ", slope, "x+", slope)
