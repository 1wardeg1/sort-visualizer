def bubbleSort(arr2):
    global operations
    arr = arr2.copy()
    moves = []
    n = len(arr)
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            operations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves.append(arr.copy())
    return [moves, operations]


arr = []
moves = []


def merge(seg1, seg2):
    global moves, arr, operations
    l1, r1 = seg1
    l2, r2 = seg2
    sortArr = arr.copy()
    ind = l1
    while l1 <= r1 and l2 <= r2:
        operations += 1
        if arr[l1] > arr[l2]:
            operations += 1
            sortArr[ind] = arr[l2]
            l2 += 1
        else:
            operations += 1
            sortArr[ind] = arr[l1]
            l1 += 1
        ind += 1
        moves.append(sortArr.copy())
    while l1 <= r1:
        operations += 1
        sortArr[ind] = arr[l1]
        l1 += 1
        ind += 1
        moves.append(sortArr.copy())
    while l2 <= r2:
        operations += 1
        sortArr[ind] = arr[l2]
        l2 += 1
        ind += 1
        moves.append(sortArr.copy())
    arr = sortArr


def recMergeSort(l, r):
    global operations
    if l == r:
        operations += 1
        return arr[0]
    mid = (l + r) // 2
    recMergeSort(l, mid)
    recMergeSort(mid + 1, r)
    merge([l, mid], [mid + 1, r])


def mergeSort(l):
    global arr, moves, operations
    arr = l.copy()
    moves = []
    operations = 0

    recMergeSort(0, len(arr) - 1)
    return [moves, operations]


operations = 0


def selectionSort(arr):
    global operations
    operations = 0
    moves = []
    for i in range(len(arr) - 1):
        min_index = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[min_index]:
                arr[k], arr[min_index] = arr[min_index], arr[k]
                moves.append(arr.copy())
                arr[k], arr[min_index] = arr[min_index], arr[k]
                moves.append(arr.copy())
                min_index = k
            operations += 1
        operations += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
        moves.append(arr.copy())
    return [moves, operations]


def insertionSort(arr):
    global operations, moves
    arr = arr.copy()
    moves = []
    operations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            operations += 1
            arr[j + 1] = arr[j]
            moves.append(arr.copy())
            j -= 1
        arr[j + 1] = key
        moves.append(arr.copy())
    return [moves, operations]


def partition(start, end):
    global moves, arr, operations
    pivot = arr[start]
    low = start + 1
    high = end
    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1
            operations += 1
        while low <= high and arr[low] <= pivot:
            low += 1
            operations += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            moves.append(arr.copy())
            operations += 1
        else:
            break
    operations += 1
    arr[start], arr[high] = arr[high], arr[start]
    moves.append(arr.copy())

    return high


def quick_sort(start, end):
    global operations
    if start >= end:
        return

    p = partition(start, end)
    quick_sort(start, p - 1)
    quick_sort(p + 1, end)


def quickSort(array):
    global arr, operations, moves
    moves = []
    arr = array.copy()
    operations = 0
    quick_sort(0, len(array) - 1)
    return [moves, operations]


def heapify(n, i):
    global moves, operations, arr
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
        operations += 1

    if r < n and arr[largest] < arr[r]:
        largest = r
        operations += 1

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        operations += 1
        moves.append(arr.copy())
        heapify(n, largest)


def heapSort(array):
    global arr, moves, operations
    moves = []
    operations = 0
    arr = array.copy()
    n = len(arr)
    for i in range(n // 2, -1, -1):
        operations += 1
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        moves.append(arr.copy())
        operations += 1
        heapify(i, 0)

    return [moves, operations]


def shellSort(array):
    global arr, moves, operations
    moves = []
    operations = 0
    arr = array.copy()
    num = len(arr)
    i = num // 2
    while i > 0:
        for j in range(i, num):
            k = j - i
            while k >= 0:
                operations += 1
                if arr[k + i] >= arr[k]:
                    break
                else:
                    arr[k], arr[k + i] = arr[k + i], arr[k]
                    moves.append(arr.copy())
                k -= i
        i //= 2

    return [moves, operations]
