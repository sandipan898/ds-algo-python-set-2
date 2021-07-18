def heapify(arr, size, index):
    smallest = index

    left = 2*index + 1
    right = 2*index + 2

    if left < size and arr[left] < arr[smallest]:
        smallest = left
    elif right < size and  arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != index:
        arr[smallest], arr[index] = arr[index], arr[smallest]
        heapify(arr, size, smallest)

def insert(arr, data):
    if len(arr) < 1:
        arr.append(data)
    else:
        arr.append(data)
        for i in range(len(arr)//2, -1, -1): # starts checking from the parent level, leaving the leaf nodes unchecked
            heapify(arr, len(arr), i)
    
def search(arr, data):
    if arr:
        left = 0
        right = len(arr)
        mid = (left + right) // 2

        if data > arr[mid]:
            return search(arr[mid+1:], data)
        elif data < arr[mid]:
            return search(arr[:mid], data)
        else:
            return mid
    else:
        return -1

def delete(arr, data):
    index = search(arr, data)
    if index != -1:
        last = len(arr) - 1
        arr[index], arr[last] = arr[last], arr[index]
        arr.remove(data)
        for i in range(len(arr)//2, -1, -1):
            heapify(arr, len(arr), i)
    else:
        return "Data Not Found!"


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)
insert(arr, 7)
insert(arr, 10)
insert(arr, 0)
print ("Max-Heap array: " + str(arr))

delete(arr, 4)
delete(arr, 9)
"""
        0 
      /   \
     3     2
   /  \   / 
  10   5 7
"""
print("After deleting an element: " + str(arr))