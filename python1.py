x = int(input("Enter the value of x: "))

numerator = 1.0
denominator = 1.0

for i in range(1, 64):
    numerator *= (x - (2 * i - 1))

for i in range(2, 65, 2):
    denominator *= (x-2 * i)

result = numerator / denominator
print("Value of the expression:", result)





