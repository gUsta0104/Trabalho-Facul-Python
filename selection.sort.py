array = [3, 6, 4, 1, 12, 324, 3456, 26, 60, 74, 23, 62, 13, 46, 37]

for i in range(len(array)):
    menor = i
    for j in range(i+1, len(array)):
        if array[menor] > array[j]:
            menor = j
    temp = array[i]
    array[i] = array[menor]
    array[menor] = temp

print(array)