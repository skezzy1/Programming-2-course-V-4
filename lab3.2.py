#Дано файл, усі компоненти якого є цілими числами, причому серед них нема нулів, а кількість додатніх чисел дорівнює кількості від’ємних. 
#У новий файл записати: а) числа так, щоб додатні чергувалися з від’ємними; б) спочатку – усі додатні, а потім – усі від’ємні; 
#в) додатні – у порядку зростання, а від’ємні – за спаданням. 
numbers = []
with open('input.txt', 'r') as file:
    for line in file:
        for number in numbers:
            if len(numbers) % 2 != 0:
                break
            elif len(positive_numbers) != len(negative_numbers):
                break
        positive_numbers = [number for number in numbers if number > 0]
        negative_numbers = [number for number in numbers if number < 0] 
        number = int(line.strip())
        numbers.append(number)
result_a = []
for pos, neg in zip(positive_numbers, negative_numbers):
    result_a.extend([pos, neg])

result_b = sorted(positive_numbers) + sorted(negative_numbers)
result_c = sorted(positive_numbers) + sorted(negative_numbers, reverse=True)

with open('output_a.txt', 'w') as file_a:
    for number in result_a:
        file_a.write(str(number) + '\n')

with open('output_b.txt', 'w') as file_b:
    for number in result_b:
        file_b.write(str(number) + '\n')

with open('output_c.txt', 'w') as file_c:
    for number in result_c:
        file_c.write(str(number) + '\n')