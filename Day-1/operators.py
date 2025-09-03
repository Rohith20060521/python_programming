def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
a=eval(input("enter num1: "))
b=eval(input("enter num2: "))
v=add(a,b)
w=sub(a,b)
x=mul(a,b)
y=div(a,b)
z=mod(a,b)
print(f"addition:{v}, subraction:{w}, multiplication:{x}, division:{y}, modulo:{z}")