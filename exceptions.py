import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: invalid input")
    sys.exit(1)#EXIT

try:
    result = x/y
except ZeroDivisionError: 
    print("Error : Cannot divide by zero")
    sys.exit(1)
finally:#executed also for the exceptions
    print("Thx")

print(f"{x} / {y} = {result}")