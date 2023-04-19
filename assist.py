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
    size = int(size)
    l = []
    for i in range (size):
        l.append(random.randrange(minimum, maximum + 1))
    return l

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       pivot = random.choice(nums)
   lowerNums = [n for n in nums if n < pivot]
   equalNums = [pivot] * nums.count(pivot)
   biggestNums = [n for n in nums if n > pivot]
   return quicksort(lowerNums) + equalNums + quicksort(biggestNums)

#def foo(*args) неорганиченное количество аргументов
#import assist as asisisis <- импортировать assist как asisisis(в коде надо будет писать это название)
#from assist import foo <- ипортирует конкретную функцию assist`а
#from assist import * <- ипортирует все функции assist`а

def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
