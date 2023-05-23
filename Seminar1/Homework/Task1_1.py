# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

print("Hi! Give a 3-digit number and I'll sum all its digits! Enter a 3-digit positive number:")
number = int(input())
if 0 < number < 1000:
    sum = 0
    while number > 0:
        sum += number%10
        number //=10
    print(f"The sum of digits is {sum}")
else:
    print("That's not a 3-digit positive number")