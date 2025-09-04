def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    return total == num
n = int(input("Enter a number: "))
if is_armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
