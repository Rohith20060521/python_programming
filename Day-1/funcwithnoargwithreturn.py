def multi():
    a=6
    b=7
    return {a,b,a*b}
mul,t,s=multi()
print(f"{s}x{t}={mul}")