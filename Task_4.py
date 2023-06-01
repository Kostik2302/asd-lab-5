steps = [1, 2, 3]

n = int(input('Введите номер ступеньки: '))
if n in [1, 2, 3]:
    print(f'Количество путей до {n} ступеньки равно {steps[n-1]}')
else:
    for i in range(3, n):
        steps.append(sum(steps[i-3:i]))
    print(f'Количество путей до {n} ступеньки равно {steps[-1]}')
