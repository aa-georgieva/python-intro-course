# 1. За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут
# длиной m километров? При решении этой задачи 
# нельзя пользоваться условной инструкцией if и циклами.

# n = int(input('Введите расстояние пройденное за день: '))
# m = int(input('Введите общее растояние: ')) 
# print(-(-m//n))


# 2. В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся
# в каждом из трех классов. Выведите наименьшее число
# парт, которое нужно приобрести для них.

# print("Введите число учеников класса «А»:")
# a = int(input())
# print("Введите число учеников класса «Б»:")
# b = int(input())
# print("Введите число учеников класса «B»:")
# c = int(input())
# print(-(-a//2+(-b//2)+-(c//2)))

# 3. Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон
# от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать невозможно.

# print("Человек бежит по перрону и вбегает вагон отъезжающего поезда. Какой по счёту от вокзала?")
# i = int(input())
# print("А ему отвечают: вы в таком-то вагоне! В каком?")
# j = int(input())
# print("Вагонов в поезде:")
# if i == j:
#     print("я не знаю")
# else:
#     print(i+j-1)

# 4. Дано натуральное число. Требуется определить, является ли
# год с данным номером високосным. Если год является високосным,
# то выведите YES, иначе выведите NO. Напомним, что в соответствии
# с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# year = int(input())
# if year%4==0 and year%100!=0 or year%400==0:
#     print("ВИСОКОСНЫЙ")
# else:
#     print("НЕ ВИСОКОСНЫЙ")
