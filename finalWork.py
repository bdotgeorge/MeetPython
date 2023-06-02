import random
import pandas as pd


def firstMethod():
    """
    with panda functions
    """
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI': lst})
    #pd.get_dummies(data)
    data['temp'] = 1 #added temp value == 1
    data.set_index([data.index, 'whoAmI'], inplace=True)
    data = data.unstack(level=-1, fill_value=0).astype(int)
    data.columns = data.columns.droplevel() #
    data.columns.name = None #remove name who am i
    print(data.head(20))

def secondMethod():
    """
    without pandas functions, 
    plus write and read file        
    """
    lst = ['robot'] * 10
    lst += ['human'] * 10
    #lst += ['animal'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI': lst})    
    print(pd.get_dummies(data))
    columns = list()
    for i in data:#to all columns
        for j in data[i].unique().tolist():
            columns.append('whoAmI_' + str(j))
    value = ''
    for c in range (0, len(columns)):
        value += str(columns[c])
        if c < len(columns) - 1: 
            value += ','
    for i in data:
        for d in data[i]:
            value += '\n'
            for v in range (0, len(columns)):
                if d in columns[v]:
                    value += str(1)
                else:
                    value += str(0)
                if v < len(columns) - 1: value += ','
    
    file = open('oneHot.csv', 'w', encoding='utf-8')
    file.write(value)
    file.close()
    
    d = pd.read_csv('oneHot.csv')
    print(f'from csv file\n {d.head(20)}') 
    print(f'from get_dummies file\n{pd.get_dummies(d)}')



firstMethod()
secondMethod()