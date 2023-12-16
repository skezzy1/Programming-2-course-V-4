import math
while True:
    x2 = float(input("Enter x2:"))
    if 0 <= x2 < 1:
        result = x2**2 - x2
    elif x2 >= 1:
        result = x2**2 + math.sqrt(x2)
    else:
        result = 0
    print("Result is:", result)

#x = int(input("Enter x:"))
#while x <=2:
#    result = x**2+4*x+5
#    print(result)
#    break
#else:
#    result = 1/(x**2+4*x+5)
#    print(result)
