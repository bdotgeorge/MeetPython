import assist
"""
for переменная in набор_значений:
message = "Hello"
 
for c in message:
    print(c)

number = 1

while условное_выражение: 
while number < 5:

"""

"""
n = int(input("Введите число Фибоначчи: "))
print((round((5*n*n+4)**0.5, 0)) == (5*n*n+4)**0.5 or (round((5*n*n-4)**0.5, 0)) == (5*n*n-4)**0.5)

y = 1
z = 2
count = 4

# while (((1+5**0.5)/2)**n-((1-5**0.5)/2)**n)/(5**0.5) < n

while z!=n:
    temp = z
    z = z+y
    y = temp
    count+=1

print(count)
"""
def factorial(number):
    if (number == 0):
        return 1;
    return number * factorial(number - 1);

def factorialWhile(number):
    if(number == 0):
        return 1
    i = 1
    fac = number
    while i < number:
        number = number - 1
        fac = fac * number
    return fac

def fibonacci(number):
    if number in (1, 2):
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

def fibonacciWhile(number):
    i = 0
    fibonacciFirst = 1
    fibonacciSecond = 1
    while i < number - 2:
        temp = fibonacciFirst + fibonacciSecond
        fibonacciFirst = fibonacciSecond
        fibonacciSecond = temp
        i += 1
    return fibonacci

"""
Уставшие от необычно теплой зимы, жители решили узнать, 
действительно ли это самая длинная оттепель за всю историю 
наблюдений за погодой. Они обратились к синоптикам, а те, в 
свою очередь, занялись исследованиями статистики за прошлые годы. 
Их интересует, сколько дней длилась самая длинная оттепель. 
Оттепелью они называют период, в который среднесуточная температура 
ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую 
синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых 
дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50


Input: 6 -> -20 30 -40 50 10 -10 Output: 2


Задача No15. Решение в группах
15. Иван Васильевич пришел на рынок и решил купить два арбуза: 
один для себя, а другой для тещи. Понятно, что для себя нужно 
выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
арбузов слишком много и он не знает как же выбрать самый легкий 
и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. 
Вторая строка содержит N чисел, записанных на новой строчке каждое. 
Здесь каждое число – это масса соответствующего арбуза

Input: 5 -> 5 1 6 5 9 Output: 1 9

"""

def sunChane(day = 6):
    tempreture = {-20, 30, -40, 50, 10, -10}
    count = 1
    hotDay = 0
    for i in tempreture:
        if(i > 0):
            count +=1
            if(hotDay < count): hotDay = count
        else:
            count = 0
    
    return hotDay



"""
Дан список чисел. Определите, 
сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
array = [2, 2, 4, 5, 6]

array2 = []

for i in array:
    if i not in array2:
        array2.append(i)

print(len(array2))

Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]
# array = input().split(",")
#
# k = int(input())
#
# for _ in range(k):
#     array.insert(0, array.pop())
#
# print(*array)

Напишите программу, которая найдёт произведение пар чисел списка.
 Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    
    *Пример:*
    
    - [2, 3, 4, 5, 6] => [12, 15, 16];
    - [2, 3, 5, 6] => [12, 15]

    
    Дан массив, состоящий из целых чисел. Напишите программу, 
которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}



"""

"""Пользователь вводит текст(строка). Словом считается последовательность непробельных 
    символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, 
    сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13

Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.


Подвиг 7. Вводятся номера телефонов в одну строчку через пробел с разными кодами стран: +7, +6, +2, +4 и т.д. 
Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., а значения - список номеров 
(следующих в том же порядке, что и во входной строке) с соответствующими кодами. Полученный словарь вывести командой:

print(*sorted(d.items()))
Sample Input:
+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890
Sample Output:
('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])

"""
def countWord(word = 'She sells sea shells on the sea shore The shells that she sells are sea shells I''m sure. So if she sells sea shells on the sea shore I''m sure that the shells are sea shore shells'):
    word.lower()
    for sep in '.,!?()[]{}':
        word.replace(sep, '')
    print(len(set(word.split())))

def countElement():
    # 1 задача
    st = input('Введите набор символов: ')
    # Input: a a a b c a a d c d d
    # Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
    chars = st.split()
    output = []
    data = {}
    for elem in chars:
        if (elem in data):
            data[elem] += 1 
        else:
            data[elem] = 1

        if (data[elem] - 1 == 0):
            output.append(elem)
        else:
            output.append(elem+f"_{data[elem]-1}")
    print(*output)

def numberWord():
    telefonNumber = ('+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890').split()
    countru = {}
    for number in telefonNumber:
        code = number[:-10]
        if(code in countru): countru[code] = number
        else: countru[code] = [number]
    print(*sorted(countru.items()))

def fib(n):
    if n in [0,1]:
        return 1
    return fib(n - 1) + fib(n - 2)

#k = 0
#for i in range (0,(int(input('')))):
#    k = fib(i)
#print(k)


def fib(n):
    if n in [0,1]:
        return 1
    return fib(n - 1) + fib(n - 2)


#print(fib(int(input())))

def reverse(array, n):
    if (n != 0):
        n -=1
        print(array[n])
        reverse(array, n)

size = 6
ar = [1, 2 ,3, 4, 5 ,6]

reverse(ar, size)