#4.	Дано дійсні числа a, b, c. Перевірити, чи справджується умова: .
#Якщо ця умова виконується, то кожне із чисел збільшити у два рази. Якщо ні, то кожне із чисел зменшити на 5.
#Результати вивести на екран.
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
collection = [a, b, c]
while a < b and b < c and a < c:
    a *= 2
    b *= 2
    c *= 2
    print("condition is right", a, b, c)
    break
else:
    a -= 5
    b -= 5
    c -= 5
    print("Condition is not right", a, b ,c)