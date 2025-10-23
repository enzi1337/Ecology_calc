import math


def marg(s, n): # s - число видов, n - общее число особей всех видов
	return round((s-1)/math.log(n), 2)


def menh(s, n): # s - число видов, n - общее число особей всех видов
	return round((s/math.sqrt(n)), 2)


def shen1(p): # p - доля вида в сообществе
	return round(p*math.log(p), 2)


def simp1(p): # p - доля вида в сообществе
	return p**2


def shen(s): # s - список, содержащий все доли видов в сообществе
	return -1*sum([shen1(x) for x in s])


def simp(s): # s - список, содержащий все доли видов в сообществе
	return round(sum([simp1(x) for x in s]), 4)


def berg(m, n): # m - количество особей доминирующего вида, n - общее кол-во особей
	return round(m/n, 2)

k = int(input('Введите общее число видов: '))
print('')
s = [] # численности видов
for i in range(1, k+1):
	s.append(float(input(f'Введите кол-во особей {i}-го вида: ')))
print('')
t = sum(s) # общая численность видов
p = [round(x/t, 2) for x in s] # доли видов
print(f'Индекс Маргалефа для данного озера: {marg(k, t)}')
print(f'Индекс Менхиника для данного озера: {menh(k, t)}')
print('Доля вида	Индекс Шеннона	 Индекс Симпсона')
for i in range(1, k+1):
	print(f'{i}:   {p[i-1]}		{shen1(p[i-1])}	  		{simp1(p[i-1])}')
print(f'Озеро: ----	 	{shen(p)}			{simp(p)}')
print('')
print(f'Индекс Бергера-Паркера: {berg(max(s), t)}')
print('')
input('Нажмите enter чтобы закрыть программу')