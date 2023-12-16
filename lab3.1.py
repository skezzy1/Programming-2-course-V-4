#Дано речення. Вилучити з цього речення усі букви ‘a’, якщо такі є, і надрукувати отримане після цього речення
def clear_letter_a(sentence):
    sentence = sentence.replace('a', '').replace('A', '')
    return sentence

input_sentence = input("Enter a sentence: ")
result = clear_letter_a(input_sentence)
print(result)