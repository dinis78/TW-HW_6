import numpy as np
import scipy.stats as stats

# Задача 1. Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a с надежностью
# 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256.
# m = 80
# s = 16
# n = 256
# alpha = stats.norm.ppf(1-0.05/2)
# a = 80+(alpha * 16) / np.sqrt(n)
# b = 80-(alpha * 16) / np.sqrt(n)
# print('Доверительный интервал для оценки математического ожидания=', round(b, 3),'< M <', round (a, 3))

######################################################################################
######################################################################################

# Задача 2. В результате 10 независимых измерений некоторой величины X, выполненных с
# одинаковой точностью,
# получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения
# вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала,
# покрывающего это
# значение с доверительной вероятностью 0,95.

# n = 10
# x = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
# alpha = stats.t.ppf(1-0.05/2, 9)
# print(alpha)
# m = np.mean(x) #среднее
# print(m)
# s = np.std(x, ddof=1) # сигма
# print(s)
# a = m + (alpha * s)/ np.sqrt(n)
# b = m - (alpha * s)/ np.sqrt(n)
# print('истинное значение величины X находится в интервале', round(b, 3), '<', 'X', '<', round (a, 3))

##############################################################################################
##############################################################################################

# Задача 3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175

# Используя эти данные построить 95% доверительный интервал для разности среднего
# роста родителей и детей.

x = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
y = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

n_1 = len(x)
n_2 = len(y)
d = np.mean(y) - np.mean(x) 
print(d)
d_o = (np.var(x, ddof=1)+np.var(y, ddof=1))/2
print(d_o)
s = np.sqrt(d_o/n_1+d_o/n_2)
print(s)
df = 2*(10-1)
print(df) 
t_k = stats.t.ppf(1-0.05/2, 18)
print(t_k)

a = d - t_k*s
b = d + t_k*s
print('доверительный интервал для разности среднего роста родителей и детей = ',a,b)

# Я так понял раз 0 включён в интервал, заначит разница не большая по росту между 
# родителями и детьми. Но почему то сам интервал большой получился? наверно из за больших чисел.
