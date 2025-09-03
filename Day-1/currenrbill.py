name=input("enter consumer name: ")
number=eval(input("enter consumer number: "))
pmr=eval(input("enter present month reading: "))
lmr=eval(input("enter last month reading: "))
total_units=pmr-lmr
costperunit=3.80
bill=costperunit*total_units
print("consumer name:",name)
print("consumer number: ",number)
print("total units: ",total_units)
print("bill amount: ",round(bill,2))