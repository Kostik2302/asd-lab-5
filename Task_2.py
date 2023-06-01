from random import randint

def find_el(i, j, matrix, k):

    if k == matrix[i][j]:
        return f'Элемент {k} дайден в ячейке {i+1}, {j+1}.'
    try:
        if k > matrix[i][j]:
            return find_el(i+1, j, matrix, k)
        else:
            return find_el(i, j-1, matrix, k)
    except:
        return f'Элемента {k} нет в матрице'

            

m = int(input('Введите количство строк: '))
n = int(input('Введите количество столбцов: '))

matrix = [[] for i in range(m)]
matrix[0].append(randint(1, 10))
for i in range(n-1):
    matrix[0].append(randint(matrix[0][i]+1, matrix[0][i]+10))

for j in range(1, m):
    matrix[j].append(randint(matrix[j-1][0]+1, matrix[j-1][0]+10))

for i in range(1, m):
    for j in range(1, n):
         matrix[i].append(randint(max(matrix[i-1][j], matrix[i][j-1])+1, max(matrix[i-1][j], matrix[i][j-1])+10))

print()
print('Сгенерированная матрица:')
for i in range(m):
    print(', '.join([str(i) for i in matrix[i]]))

print()
k = int(input('Введите искомый элемент: '))

print(find_el(0, n-1, matrix, k))


