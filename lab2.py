#Ввод переменных с клавиатуры
a = input ('Введите первое число: ')
b = input ('Введите второе число: ')
c = input ('Введите третье число: ')
#Условие вывода
if a<b<c or a<c<b:
    min = a
if b<a<c or b<c<a:
    min = b
if c<a<b or c<b<a:
    min = c
#Вывод наименьшего числа из введённых
print ('Наименьшее число: ', min)

#Задание 1.2
#Ввод переменных с клавиатуры
print('Введите три произвольных числа: ')
a = int(input())
b = int(input())
c = int(input())
#Условие вывода
if 1 <= a <= 50:
    print(a)
if 1 <= b <= 50:
    print(b)
if 1 <= c <= 50:
    print(c)


#Задание 1.3
#Ввод переменных с клавиатуры
print ('Введите вещественное число')
m = float(input("m: "))
#Цикл
for z in range(1,11):
    print (z*m)

#Задание 1.4

#Объявление переменных
s = 0
q = 0
#Вывод информационного сообщения
print('Для заверщения ввода последовательности введите 0')
num = int(input('Введите число: '))
#Цикл
while num != 0:
    #Суммирование введённых значений
    s += num
    #С каждым кругом выполнения к количеству прибавляется 1
    q += 1
    #Действие, выполняемое циклом
    num = int(input('Введите число: '))
#Вывод результатов
print('Сумма: ', s)
print('Количество: ', q)



#Задание 2.2
string = input("Введите строку: ")
count = string.count(":")
string = string.replace(":", "%")
print("Количество замен:", count)
print("Результат замены:", string)

#Задание 3.2
import sys
arr = list(map(int, sys.argv[1:]))
min_element = arr[0]
min_index = 0
for i in range(1, len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]
        min_index = i
print("Индекс минимального элемента:", min_index)
positive_elems = [str(elem) for elem in arr if elem > 0]
print("Положительные элементы:", " ".join(positive_elems))
negative_elems = [str(elem) for elem in arr if elem < 0]
print("Отрицательные элементы:", " ".join(negative_elems))
