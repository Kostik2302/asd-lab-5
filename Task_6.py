import matplotlib.pyplot as plt

from random import randint

Katya = [randint(-10, 10) for i in range(100)]
new_Katya = []

print(f'Созданная функция: {Katya}')

def exp_filter(f, s_k=0.2, max_k=0.9, d=1.5):
    if not hasattr(exp_filter, "fit"):
        exp_filter.fit = f

    k = s_k if (abs(f - exp_filter.fit) < d) else max_k

    exp_filter.fit += (f - exp_filter.fit) * k

    return exp_filter.fit

for i in Katya:
    new_Katya.append(exp_filter(i))

plt.plot(Katya, 'b', label='Исходная последовательность')
plt.plot(new_Katya, 'g', label='Фильтрованная последовательность')
plt.legend(fontsize=8)

plt.show()