#Трикутник заданий координатами його вершин. Знайти: периметр трикутника; площу трикутника.
import math
#x1 = int(input("Enter x1:"))
#x2 = int(input("Enter x2:"))
#y1 = int(input("Enter y1:"))
#y2= int(input("Enter y2"))
#z1 = int(input("Enter z1:"))
#z2 = int(input("Enter x2:"))
x1, y1 = 0, 0
x2, y2 = 2, 1
x3, y3 = 5, 0
a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
c = math.sqrt((x1-x3)**2 + (y1-y3)**2)
perimetr = a + b + c
half_perimetr = perimetr / 2
s = math.sqrt(half_perimetr*(half_perimetr-a)*(half_perimetr-b)*(half_perimetr-c))
print("Perimetr: ", perimetr , "Area:", s)