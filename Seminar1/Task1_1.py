# 1. За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут
# длиной m километров? При решении этой задачи 
# нельзя пользоваться условной инструкцией if и циклами.

n = int(input('Введите расстояние пройденное за день: '))
m = int(input('Введите общее растояние: ')) 
print(-(-m//n))