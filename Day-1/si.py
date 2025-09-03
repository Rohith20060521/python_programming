p=eval(input("enter principle amount: "))
t=eval(input("enter time taken : "))
r=eval(input("enter rate of interest: "))
si=(p*t*r)/100
print("simple interest: ",si)
totalamount=si+p
print("total amount: ",totalamount)