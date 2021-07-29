def heapify(arr, size, index):
    largest = index
    left = 2*index + 1
    right = 2*index + 2

    if left < size and arr[largest] < arr[left]:
        largest = left
    if right < size and arr[largest] < arr[right]:
        largest = right
    
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, size, largest)

def enqueue(arr, data):
    size = len(arr)
    if size == 0:
        arr.append(data)
    else:
        arr.append(data)
        for i in range(len(arr)//2, -1, -1):
            heapify(arr, len(arr), i)
    print("{} Inserted!".format(data))

def search(arr, data):
    for i in arr:
        if i == data:
            return arr.index(i)
    return -1

def dequeue(arr, data):
    size = len(arr)
    index = search(arr, data)
    if index == -1:
        print("Element with value {} can not be found!".format(data))
        return False
    arr[index], arr[size-1] = arr[size-1], arr[index]
    arr.pop(size - 1)
    print("{} Deleted!".format(data))
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, len(arr), i)
    return True

def get_max(arr):
    if len(arr) != 0:
        return arr[0]
    return None

def display(arr):
    print("Queue:")
    for i in arr:
        print("{} | ".format(i), end="")
    print()


if __name__ == '__main__':
    arr = []
    enqueue(arr, 1)
    enqueue(arr, 4)
    enqueue(arr, 2)
    enqueue(arr, 8)
    display(arr)
    dequeue(arr, 4)
    dequeue(arr, 5)
    display(arr)
    print("Max Value: ", get_max(arr))