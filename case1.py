"""
Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""
from pandas import read_csv

data = read_csv('california_housing_test.csv')

print(data.info())
print(data.describe())
print(data.shape)
print(data.dtypes)

print(type(data))