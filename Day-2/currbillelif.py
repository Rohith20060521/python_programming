def check(x):
    if(x>=1 and x<=50):
        bill=x*3.80
    elif(x>50 and x<=100):
        bill=(50*3.80)+((x-50)*4.20)
    elif (x>100 and x<=200):
        bill=(50*3.80)+(50*4.20)+((x-100)*5.10)
    elif (x>200 and x<=300):
        bill=(50*3.80)+(50*4.20)+(100*5.10)+((x-200)*6.30)
    else:
        bill=(50*3.80)+(50*4.20)+(100*5.10)+(100*6.30)+((x-300)*7.50)
    return bill
name=input("enter consumer name: ")
number=eval(input("enter consumer number: "))
pmr=eval(input("enter present month reading: "))
lmr=eval(input("enter last month reading: "))
total_units=pmr-lmr
print("consumer name:",name)
print("consumer number: ",number)
print("total units: ",total_units)
x=check(total_units)
print("bill: ",x)