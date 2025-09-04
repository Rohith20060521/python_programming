def check(x):
    if x.isupper():
        return " capital alphabet"
    elif x.islower():
        return "small alphabet"
    elif x.isdigit():
        return "digit"
    else:
        return "special char"
x=input("enter character: ")
y=check(x)
print(y)