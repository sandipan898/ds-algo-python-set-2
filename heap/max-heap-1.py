def heapify(arr, size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < size and arr[left] > arr[index]:
        largest = left
    if right < size and arr[right] > arr[index]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        print("Swapped")
        heapify(arr, size, largest)
    return arr

def insert(arr, el):
    if len(arr) == 0:
        arr.append(el)
    elif len(arr) > 0:
        arr.append(el)
        for i in range((len(arr)//2)-1, -1, -1):
            heapify(arr, len(arr), i)

def search(arr, el):
    if len(arr) > 0:
        for i in range(len(arr)):
            if arr[i] == el:
                return i
    return -1

def delete(arr, el):
    index = search(arr, el)
    if index==-1:
        return False
    arr[index], arr[len(arr)-1] = arr[len(arr)-1], arr[index]
    arr.remove(el)
    for i in range((len(arr)//2)-1, -1, -1):
        heapify(arr, len(arr), i)

# arr1 = [3, 9, 2, 1, 4, 5]
# for i in range(len(arr1), -1, -1):
#     arr1 = heapify(arr1, len(arr1), i)
arr1 = []
insert(arr1, 3)
insert(arr1, 4)
insert(arr1, 9)
insert(arr1, 5)
insert(arr1, 2)
print(arr1)
delete(arr1, 4)
print(arr1)
