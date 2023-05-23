# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют
# такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket_num = int(input("Input a ticket number: "))
sum_first = 0
sum_last = 0
if 1000000 > ticket_num > 0:
    while ticket_num > 0:
        if ticket_num > 999:
            sum_first += ticket_num%10
        else:
            sum_last += ticket_num%10
        ticket_num //= 10
    print(f"The ticket is lucky: {sum_first == sum_last}")
else:
    print("That's wrong ticket number")
