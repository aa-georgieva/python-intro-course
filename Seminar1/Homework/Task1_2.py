# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов
# сделал каждый ребенок, если известно, что Петя
# и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

total = int(input("Input total number of paper cranes: "))
if total % 6 == 0:
    anyboy = int(total/6)
    katya = int(anyboy*4)
    print(f"Petya and Serezha made {anyboy} cranes each, Katya made {katya} cranes.")
else:
    print("That's incorrect total number.")
