import pandas as pd
import scipy as scp
from scipy.stats import spearmanr
import xlwt

# test_series = pd.Series([1, 1, 3, 1, 5])
# test_series[test_series == 1] = 9
# print(test_series)
conv_map = {
    'Полностью согласен': 5,
    'Согласен': 4,
    'Не определился': 3,
    'Не согласен': 2,
    'Совсем не согласен': 1,

    'Да': 3,
    'Нет': 2,
    'Затрудняюсь ответить': 1,
    'Другое': 5,

    'слишком сложно': 4,
    'вполне доступно': 3,
    'слишком примитивно': 2,

    'слишком быстрый': 3,
    'приемлемый': 2,
    'слишком медленный': 1,

    'Не вижу связи': 1,

    'Не присутствовал на аудиторных занятиях': 1,

    'Да, регулярно': 4,
    'Весьма эпизодически': 3,

    'Воздержусь': 1,

    'Не всегда': 1,

    'Я не спрашивал': 1,

    'Однозначно, да': 4,
    'Некоторые рекомендации были полезны': 3,
    'Нет, время на их чтение потрачено зря': 2,
    'Зачем читать методичку, если есть работы одногруппников?': 1,

    'посильный': 3,
    'не посильный': 2,

    'Всегда': 3,
    'Иногда': 2,
    'Никогда': 1,

    'самостоятельно': 4,
    'с небольшой помощью': 3,
    'часто требовалась помощь': 2,
    'всегда списывал': 1,

    '90-100': 5,
    '75-89': 4,
    '60-74': 3,
    '31-59': 2,
    '0-30': 1
}
data = pd.read_csv('seps_utf.csv', ';')
data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
data = data.drop(['Оценка', 'Группа'], 1)
data = data.dropna()
data = data.applymap(lambda el: conv_map.get(el, 5))
i = 0
j = 0
correlation_res = []
for up_row in data.items():
    row_res = []
    # print(up_row[0])
    for left_row in data.items():
        cf, p = spearmanr(up_row[1], left_row[1])
        row_res.append((round(cf, 4), round(p, 4)))
    correlation_res.append(row_res)
# print(correlation_res)
res_data = pd.DataFrame(correlation_res)
res_data = res_data.rename(columns=lambda x: data.columns[x], index=lambda x: data.columns[x])
res_data.to_csv(r'testing.csv')
res_data.to_excel('testing_x.xls')
# data = pd.DataFrame({'k1': ['v11', 'v12', 'v13'], 'k2': ['v21', 'v22', 'v23'], 'k3': ['v31', 'v32', 'v33'], 'k4': ['v41', 'v42', 'v43']})
# i = 0
# for top_items in data.items():
#     print(top_items)
#     print('===== ' + str(i))
#     i+=1
    # for left_items in data.items():
    #     coef, p = spearmanr()
m1 = pd.Series([1, 2, 3, 4])
m2 = pd.Series([2, 3, 4, 5])

# cf, p = spearmanr(m1, m2)
# print((cf, p))
# print(p)
# i = 0
# for s in data.values:
#     print(i)
#     print(s)
#     i+=1
# print(data.drop([data.index.count:]))

