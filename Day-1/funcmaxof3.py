def max(a,b,c):
    if a>b:
        if a>c:
            print(f"a={a} is max")
        else:
            print(f"c={c} is max")
    else:
        if b>c:
            print(f"b={b} is max")
        else:
            print(f"c={c} is max")
a=int(input("enter num1: "))
b=int(input("enter num2: "))
c=int(input("enter num3: "))
max(a,b,c)