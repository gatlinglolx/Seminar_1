# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input())
res = (s // 3) // 2
petya = serega = res
katya = s - (petya + serega)
if s % 2 == 0:
    print(s , '->', petya, katya, serega)
else: 
    print('Неверное S')    
