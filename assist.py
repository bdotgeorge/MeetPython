def takeConsole(message = 'enter number'):
    result = input(message + '\n')
    return result

def takeFist(value):
    first = int(value)
    while first > 10:
        first = first // 10
    return first

def takeMid(value):
    mid = int(value)
    mid = (mid // 10) - takeFist(mid) * 10
    return mid

def takeLast(value):
    last = int(value) % 10
    return last