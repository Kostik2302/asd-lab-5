from random import randint

a = []
l = 0

c = randint(-100, 100)

shift = randint(1, 100)
while l < 100:
    k = randint(c, c+100+shift)
    if k not in a:
        a.append(k)
        l += 1

print('Сучайная последовательность уникальных чисел:')
print(a)
print()
print('Отсортированная последовательность (для проверки):')
print(sorted(a))
print()

m = min(a)
n = len(a)
us = [False] * (n+1)
for x in a:
    if x <= m+n:
        us[x-m] = True
 
for i in range(0, n + 1):
    if not us[i]:
        print(f'Пропущенный элемент: {i + m}')
        break