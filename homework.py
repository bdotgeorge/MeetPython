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
    assist.sumAllNumberNum(number)
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


