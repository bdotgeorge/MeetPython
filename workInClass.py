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

"""
