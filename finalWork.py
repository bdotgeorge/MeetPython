import random
import pandas as pd


def pandasMethod():
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
    print(f'Pandas method\n{data}')

def myMethod():
    print('My method\n')
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI': lst})    
    #print(pd.get_dummies(data))
    columns = dict()
    value = list()
    """    for i, j in enumerate(data):
        print(f'data {i, j}\n')
    """
    for i in data:#to all columns
        for k, j in enumerate(data[i].unique().tolist()):
            columns[j] = k
    z = pd.DataFrame()
    for i in data:
        for d in data[i]:
            columns.get(d)
            z[d] = columns.get(d)
    print(data.size)
    print(z)


#pandasMethod()
myMethod()