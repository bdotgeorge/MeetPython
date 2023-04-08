import assist


def enterTaskNumber():
    """
    Переключает между задачами
    """
    taskNum = int(assist.takeConsole('Enter task number, or press 0 to exit'))
    if(taskNum == 2):
        taskTwo(assist.takeConsole('Введите трех значное число'))
        enterTaskNumber()
    elif(taskNum == 4):
        taskFour('Ведите количество журавлей')
        enterTaskNumber()
    elif(taskNum == 6):
        taskSix(assist.takeConsole('Введите номер билетика'))
        enterTaskNumber()
    elif(taskNum == 8):
        chocolate(3, 2, 1)
        enterTaskNumber()
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
    while number > 1000:
        number = number // 10

    first = assist.takeFist(number)
    mid = assist.takeMid(number)
    last = assist.takeLast(number)
    print(first + mid + last)


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
    while happyNumber > 1_000_000:
        happyNumber // 10
    left = happyNumber // 1000
    right = happyNumber % 1000
    left = (assist.takeFist(left) + assist.takeMid(left) + assist.takeLast(left))
    right = (assist.takeFist(right) + assist.takeMid(right) + assist.takeLast(right))
    happy = True
    if(left != right): happy = False
    if(happy):
        print('Yes. Happy ticket')
    else:
        print('No. Next time')


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


