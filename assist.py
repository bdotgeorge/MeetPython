import random

def takeConsole(message = 'enter number'):
    result = input(message + '\n')
    return result

def takeFist(value):
    first = int(value)
    while first >= 10:
        first = first // 10
    return first

def takeMid(value):
    mid = int(value)
    mid = (mid // 10) - takeFist(mid) * 10
    return mid

def takeLast(value):
    last = int(value) % 10
    return last

def takeConsoleToList(message = 'enter number'):
    list = input(message + '\n').split(',')
    return list

def sumAllNumberNum(number):
    number = int(number)
    result = 0
    while(number > 0):
        result = result + (number % 10)
        number = number //10
    return result

def fillList(size = 8, minimum = 0, maximum = 1):
    list = []
    for i in range (size):
        list.append(random.randrange(minimum, maximum + 1))
    return list

