def con(i):
    if i=="1":
        return "one"
    elif i=="2":
        return "two"
    elif i=="3":
       return "three"
    elif i=="4":
        return "four"
    elif i=="5":
        return "five"
    elif i=="6":
      return "six"
    elif i=="7":
       return "seven"
    elif i=="8":
        return "eight"
    elif i=="9":
        return "nine"
a=int(input("enter num: "))
for i in str(a):
    print(con(i),end=" ")