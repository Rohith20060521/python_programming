import math
a=eval(input("enter radius of cylinder: "))
b=eval(input("enter height of cylinder: "))
vol=math.pi*a*a*b
ans=round(vol,2)
print("volume of cylinder: ",ans)