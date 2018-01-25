#Daniel
#1/25/18
SideA=float(input("Input side A please "))
SideB=float(input("Input side B please "))
SideC=float(input("Input side C please "))

great=max(SideA, SideB, SideC)
least=min(SideA, SideB, SideC)
mid=(SideA+SideB+SideC)-great-least
print( great > least + mid)
