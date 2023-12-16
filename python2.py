#4.	Дано сторону основи та висоту правильної чотирикутної піраміди. Обчислити її об’єм та знайти повну площу поверхні.
x = int(input("Enter x:"))
h = int(input("Enter h:"))
S = x**2
V = (1/3)*S*h
P = 4*x
A_bitchna = (1/2)*P*h
A_povna = S+A_bitchna
print("Povna:", A_povna, "V:", V)