#"Числа и арифметические операции"
#1 Работа с целыми и вещественными числами

a = 1
b = 2
x= 2.5
y = -4.6
print(a,type(a))
print(b,type(b))
print(x,type(x))
print(y,type(y))

#2. Основные арифметические операции

num1 = 2
num2 = 4

print("Сложение",num1 + num2)
print("Разность",num1 - num2)
print("Умножение",num1 * num2)
print("Деление",num1 / num2)
print("Целочисленное деление",num1 // num2)
print("Остаток от деление",num1 % num2)
print("Возведение в степень", num1 ** num2)

#3. Особенности работы с делением

a=10
b=-3
print(a / b )
print(a // b )
print(a % b )

#4. Работа с приоритетом операторов

print(5 + 3 * 2)
print((5 + 3) * 2)
print(10 / 2 ** 2)

#5. Использование сокращенных операторов
count = 10
count +=5
count -=3
count *=2
count /=4

print(count)

#"Строки в Python".
#1. Создание строк
s1 = "Python"
s2 = "Программирование"
print(s1,s2)
s3 = """Питон это
язык
программирования
"""
print(s3)
empty = ""
print(len(empty))

#2. Конкатенация строк

first_name = "Иван"
last_name = "Петров"
full_name = first_name + " " + last_name
print(full_name)

#3. Преобразование типов

s = "Возраст: "
age = 25

result = s + str(age)
print(result)

#4. Дублирование строк

ha = "ха"
ha5 = ha * 5
print(ha5)

#ha25 = ha *2.5
#print(ha25)
#Не получилось, выдало ошибку TypeError: can't multiply sequence by non-int of type 'float'

#5. Длина строки

text = "Привет, мир!"
print(len(text))

#6. Проверка вхождения подстроки
sentence = "Я изучаю Python"
print("Python" in sentence)
print("Java" in sentence)

#7. Сравнение строк

a = "apple"
b = "banana"
print(a == b)   # равно ли
print(a != b)   # не равно ли
print(a < b)    # меньше ли (по алфавиту)
print(a > b)    # больше ли
print(a <= b)   # меньше или равно
print(a >= b)   # больше или равно

#8. Код символов

print(ord('А'))
print(ord('а'))
print(ord('Я'))




