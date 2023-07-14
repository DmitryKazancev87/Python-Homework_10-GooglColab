# Задание 44:
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head()


import random
# import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)  
# Функция shuffle() модуля random перемешивает изменяемую
# последовательность x на месте. Функция ничего не возвращает, а изменяет непосредственно
# сам объект последовательности x.
print(lst)
print()
# data = pd.DataFrame({'whoAmI':lst})
#  -- Dataframe двумерное (таблица) мзмерение в Pandas,
# а Series - одномерное измерение (строка) в pandas.
# data.head() По умолчанию функция head() отображает первые пять строк DataFrame в Pandas
# data.loc[data['whoAmI'] == 'robot', 'robot_team'] = '1'
# data.loc[data['whoAmI'] != 'robot', 'robot_team'] = '0'
# data.loc[data['whoAmI'] == 'human', 'human_team'] = '1'
# data.loc[data['whoAmI'] != 'human', 'human_team'] = '0'
# data.head(20)