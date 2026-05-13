def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array [j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

numeros = [2, 4, 6, 3, 5, 6, 32, 1243, 756, 2345, 867, 85, 63, 14, 25]
bubbleSort(numeros)
print(numeros)