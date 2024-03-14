#Бинарный поиск (O(log n))
def binarySearch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binarySearch(my_list, 7))
print(binarySearch(my_list, 2))


#Сортировка выбором (O(n2))
def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selectionSort(array):
    new_array = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        new_array.append(array.pop(smallest))
    return new_array

print(selectionSort([5, 3, 6, 2, 10]))