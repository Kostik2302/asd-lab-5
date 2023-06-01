def queen(y, coords_list):
    global n
    for i in range(8):
        flag = 0
        for coords in coords_list:
            if i == coords[0] or abs(i - coords[0]) == abs(y - coords[1]):
                flag = 1      
        if flag == 0: 
            if y == 7:
                n += 1
            else:
                k = coords_list.copy()
                k.append([i, y])
                queen(y+1, k)

n = 0
for i in range(8):
    queen(1, [[i, 0]])

print(f'Количество расстановок: {n}')
