import assist
import sys

def enterTaskNumber():
    """
    Переключает между задачами
    """
    taskNum = int(assist.takeConsole('Enter task number, or press 0 to exit'))
    if(taskNum == 2):
        taskTwo(assist.takeConsole('Введите трех значное число'))
        enterTaskNumber()
    elif(taskNum == 4):
        taskFour(assist.takeConsole('Ведите количество журавлей'))
        enterTaskNumber()
    elif(taskNum == 6):
        taskSix(assist.takeConsole('Введите номер билетика'))
        enterTaskNumber()
    elif(taskNum == 8):
        chocolateSize = assist.takeConsoleToList('Enter chocolate bar size (W, H)')
        if len(chocolateSize) < 2: return print('The size is incorrect')
        width = int(chocolateSize[0])
        height = int(chocolateSize[1])
        slice = int(assist.takeConsole('Enter the size of the slices'))
        chocolate(width, height, slice)
        enterTaskNumber()
    elif(taskNum == 10):
        list = assist.fillList()
        print(list)
        print(coins(list))
    elif(taskNum == 14):
        task14(int(input('Enter number\n')))
    elif(taskNum == 12):
        task12()
    elif(taskNum == 16):
        task16(assist.takeConsole('set list size'))
    elif(taskNum == 18):
        task18()
    elif(taskNum == 20):
        task20()
    elif(taskNum == 22):
        task22()
    elif(taskNum == 24):
        task24()
    elif(taskNum == 26):
        print(myPowRec(int(assist.takeConsole()), int(assist.takeConsole('exponent'))))
    elif(taskNum == 28):
        task28()
    elif(taskNum == 0):
        print('Exit')
    else:
        print('There is no task with this number')
        enterTaskNumber()

def taskTwo(number): 
    """
    Найдите сумму цифр трехзначного числа.
    """
    number = int(number)
    if (number < 100 or number > 1000): return print('non three digit number ')
    #assist.sumAllNumberNum(number)
    print(assist.sumAllNumberNum(number))


def taskFour(number):
    """
    Петя, Катя и Сережа делают из бумаги журавликов. 
    Вместе они сделали S журавликов. Сколько журавликов 
    сделал каждый ребенок, если известно, что Петя и 
    Сережа сделали одинаковое количество журавликов, а
    Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе
    """
    number = int(number)
    girl = (number // 3) * 2
    boys = (number - girl) // 2
    correct = True
    if((girl + (boys * 2)) != number): correct = False
    if(correct):
        print(f'girl made {girl} crane, boys did {boys} each')
    else:
        print('proportion not working')

def taskSix(happyNumber):
    """
    Вы пользуетесь общественным транспортом? 
    Вероятно, вы расплачивались за проезд и получали билет с номером. 
    Счастливым билетом называют такой билет с шестизначным номером, 
    где сумма первых трех цифр равна сумме последних трех. 
    Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
    """
    happyNumber = int(happyNumber)
    if(happyNumber < 100_000 or happyNumber > 1_000_000): return print('Not correct number')
    if(assist.sumAllNumberNum(happyNumber // 1000) == assist.sumAllNumberNum(happyNumber % 1000)): 
        print('Yes. Happy ticket')
    else: print('No. Next time')

def chocolate(wight, height, pice):
    """
    Требуется определить, можно ли от шоколадки 
    размером n × m долек отломить k долек, если 
    разрешается сделать один разлом по прямой между 
    дольками (то есть разломить шоколадку на два прямоугольника).
    """
    if (pice < wight * height and ((pice % wight == 0) or (pice % height == 0))):
        print('Yes')
    else:
        print('No')

def coins(listCoin):
    eagleCount = 0
    tailsCount = 0
    for i in listCoin:
        if(i == 1): eagleCount +=1
        elif(i == 0): tailsCount +=1
    return min(eagleCount, tailsCount)

def task14(N):
    number = 2
    i = 0
    while number ** i <= N:
        print(number ** i)
        i+=1

def task12(a = 5, b = 6):
    res = list()
    a = int(a)
    b = int(b)
    for i in range(a + b):
        if i == (a * i - b)**0.5:
            res.append(i)
    print(*res if len(res) == 2 else res + res)


def task16(sizeArray = 5):
    """
    Требуется вычислить, сколько раз встречается некоторое 
    число X в массиве A[1..N]. Пользователь в первой строке 
    вводит натуральное число N – количество элементов в массиве. 
    В последующих  строках записаны N целых чисел Ai. 
    Последняя строка содержит число X
    """
    sizeArray = int(sizeArray)
    numbers = assist.fillList(sizeArray, sizeArray // 2, sizeArray ** 2)
    searchElement = int(assist.takeConsole('enter searchig element'))
    count = int(0)
    if (searchElement not in numbers):
        return print(f'the list does not contain such an element {searchElement} no in {numbers}')
    for i in numbers:
        if(i == searchElement): count +=1
    print(f'The element you are looking for is found in the list = {count} in {numbers}')

def task18(sizeArray = 8):
    """
    Требуется найти в массиве A[1..N] 
    самый близкий по величине элемент к заданному числу X. 
    Пользователь в первой строке вводит натуральное число 
    N – количество элементов в массиве. 
    """
    sizeArray = int(sizeArray)
    numbers = assist.fillList(sizeArray, sizeArray // 2, sizeArray ** 2)
    nearestElement = int(assist.takeConsole('enter nearest element'))
    #numbers = assist.quicksort(numbers)
    numbers.sort()
    left = int(0)
    right = int(len(numbers) - 1)
    mid = left
    containt = False
    #temp = -sys.maxsize
    temp = abs(nearestElement - numbers[left])
    find = numbers[left]
    while(containt == False and left <= right):
        mid = (left + right) // 2
        if(numbers[mid] == nearestElement): containt = True
        elif(numbers[mid] > nearestElement): 
            right = mid - 1
            if(abs(nearestElement - numbers[mid]) < temp):
                temp = abs(nearestElement - numbers[mid])
                find = numbers[mid]
        else: 
            left = mid + 1
            if(abs(nearestElement - numbers[mid]) < temp):
                temp = abs(nearestElement - numbers[mid])
                find = numbers[mid]

    if(containt == True):
       return print(f'Found exact match = {numbers[mid]} in {numbers}')
    print(f'The element you are looking for is found in the list = {find} in {numbers}')

def task20():
    """
    Напишите программу, которая вычисляет стоимость введенного 
    пользователем слова. Будем считать, что на вход подается 
    только одно слово, которое содержит либо только английские, 
    либо только русские буквы.
    """
    points = {'1': 'AEIOULNSTRАВЕИНОРСТ', 
              '2': 'DGДКЛМПУ',
              '3': 'BCMPБГЁЬЯ',
              '4': 'FHVWYЙЫ',
              '5': 'KЖЗХЦЧ',
              '8': 'JXШЭЮ',
              '10' : 'QZФЩЪ'}
    points2 = {'AEIOULNSTRАВЕИНОРСТ': '1', 
              'DGДКЛМПУ': '2',
              'BCMPБГЁЬЯ': '3',
              'FHVWYЙЫ': '4',
              'KЖЗХЦЧ': '5',
              'JXШЭЮ': '8',
              '1QZФЩЪ' : '10'}
    word = assist.takeConsole('Enter word')
    word = word.upper()
    score = 0
    for i in word:
        for k in points:
            if(i in points.get(k)):
                score += int(k) 
    print(f'score = {score}')

def task22():
    """
    Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
    Выдать без повторений в порядке возрастания все те числа, которые встречаются 
    в обоих наборах.
    Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
    m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
    """
    firstSize = int(assist.takeConsole('введите размер множества'))
    firstList = list()
    secondList = list()
    i = 0
    while i < firstSize:
        value = int(assist.takeConsole(f'введите {i + 1} из {firstSize} элемент множества'))
        firstList.append(value)
        i += 1
    secondSize = int(assist.takeConsole('введите второго размер множества'))
    i = 0
    while i < secondSize:
        value = int(assist.takeConsole(f'введите {i + 1} из {firstSize} элемент множества'))
        secondList.append(value)
        i += 1
    temp = set(firstList) & set(secondList)
    result = assist.quicksort(list(temp))
    print(result)

def task24():
    """
    В фермерском хозяйстве в Карелии выращивают чернику. 
    Она растёт на круглой грядке, причём кусты высажены только по окружности. 
    Таким образом, у каждого куста есть ровно два соседних. 
    Всего на грядке растёт N кустов.
    Эти кусты обладают разной урожайностью, поэтому ко 
    времени сбора на них выросло различное число 
    ягод — на i-ом кусте выросло ai ягод.
    В этом фермерском хозяйстве внедрена система 
    автоматического сбора черники. Эта система состоит 
    из управляющего модуля и нескольких собирающих модулей. 
    Собирающий модуль за один заход, находясь непосредственно 
    перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
    Напишите программу для нахождения максимального числа ягод, 
    которое может собрать за один заход собирающий модуль, 
    находясь перед некоторым кустом заданной во входном файле грядки.
    """
    numberOfBushes = 7
    berries = list()
    for i in range(numberOfBushes):
        berries.append(int(assist.takeConsole()))
    berriesCount = list()
    for i in range(len(berries) - 1):
        berriesCount.append(berries[i - 1] + berries[i] + berries[i + 1])
    berriesCount.append(berries[-2] + berries[-1] + berries[0])
    print(max(berriesCount))

def myPowRec(a, b):
    if(b == 1):
        return a
    b -= 1
    return a * myPowRec(a, b)

#print(myPowRec(int(assist.takeConsole()), int(assist.takeConsole('exponent'))))
def sumNumber(a, b):
    if(b == 0): return a
    a += 1
    b -= 1
    return sumNumber(a, b)

def task28():
    a = int(assist.takeConsole())
    b = int(assist.takeConsole())
    if(a < 0 or b < 0):
        print('negative numbers')
    else:
        print(sumNumber(a, b))