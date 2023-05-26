import pandas as pd

"""    
Самостоятельная практика №1
Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
Посмотреть сколько в нем строк и столбцов
(Доп) Определить какой тип данных имеют столбцы
(Доп) Проверить есть ли в файле пустые значения
"""
    
    
df = pd.read_csv('sample_data/california_housing_test.csv')
df.shape
df.dtypes
df.isnull()
df.isnull().sum()

"""
Самостоятельная практика №2
Показать median_house_value где median_income < 2
(Доп) Показать данные в первых 2 столбцах
(Доп) Выбрать данные где housing_median_age < 20 и median_house_value > 70000
"""
df[(['median_house_value']) & (df['median_income'] < 2)]
df[['longitude', 'latitude']]
df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]

"""
Самостоятельная практика №3
Определить какое максимальное и минимальное значение median_house_value
(Доп) Показать максимальное median_house_value, где median_income = 3.1250
(Доп) Узнать какая максимальная population в зоне минимального значения median_house_value

"""
df['median_house_value'].max()
df[(['median_house_value']) & (df['median_income'] == 3.1250)].max()