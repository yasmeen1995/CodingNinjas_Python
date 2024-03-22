def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    
def heapify(arr, n, pos):
    idx = pos
    while 2 * idx <= n:
        g = idx
        left = 2 * idx
        right = 2 * idx + 1
        if arr[idx] < arr[left]:
            g = left
        if right <= n and arr[right] > arr[g]:
            g = right

        if g == idx:
            break

        swap(arr, g, idx)
        idx = g



if __name__ == "__main__":
    arr = [0,4,2,3,7,6,5]
    n = 6

    for i in range(n, 0, -1):
        heapify(arr, n, i)

    # arr is max heap?
    print(arr)


    # heap sort algo

    for i in range(n, 0, -1):
        swap(arr, 1,i)
        heapify(arr, i-1, 1)
        print("sorted array")
        print(arr)