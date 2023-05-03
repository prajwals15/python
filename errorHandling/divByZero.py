def divison(dividend, divisor):
    try:
        return str(dividend/divisor)
    except ZeroDivisionError:
        print("Error: You are trying to divide by 0")


print(divison(33, 10))
print(divison(24, 2))
print(divison(100, 0))
print(divison(6, 4))
