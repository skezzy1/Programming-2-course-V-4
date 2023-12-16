import math
brave = int(input("Enter brave from 0 to 100:"))
intelligence = int(input("Enter inteligence from 0 to 100:"))
persistence = int(input("Enter persistence from 0 to 100:"))
ambitions = int(input("Enter ambitions from 0 to 100:"))
qualities = [brave, intelligence, persistence, ambitions]
max_quality = max(qualities)

if max_quality == brave:
    print("Ґрифіндор")
elif max_quality == intelligence:
    print("Рейвенклов")
elif max_quality == persistence:
    print("Гафелпаф")
else:
    print("Слизирин")