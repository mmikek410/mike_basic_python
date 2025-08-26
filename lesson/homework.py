#1. Создание переменных и вывод значений
name = "Mike"
age = 24
height = 190.5

print("Меня зовут", name, ", мой возраст" ,age , "года и мой рост" ,height)

#2. Изменение значений переменных

x = 10
print(type(x))
x = 25.5
print(type(x))
x = "Python"
print(type(x))

#3. Копирование ссылок

a = 7
b = a
print(a, b)
a = 10
print(b, "Значение не изменилось тк объект b был присовен к объекту а, когда он был равен 7")

#4. Каскадное присваивание

x = y = z = 100
print(id(x),id(y),id(z))
x,y,z = 100, 101, 102
print(id(x),id(y),id(z))

#5. Обмен значений переменных

a = 5
b = 10
b,a = a, b
print(a,b)

#6. Работа с именами переменных
print("Переменные с назваиями True, print, if нельзя создать, так как это ключевые слова Python, при  создании переменных с таким именем возникнет ошибка")
import keyword
print(keyword.kwlist)

#7 Использование функции type()

var1 = 42
var2 = 3.14
var3 = "Hello"

print(type(var1),type(var2),type(var3))

var1 = "Godd Bye"
print(type(var1))

# 8. Дополнительные задания
a, b, c,d,e = 10, 20, "Тридцать", 40.0, 50
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
Число = 50
print(Число)
#переменная с русским названием работает