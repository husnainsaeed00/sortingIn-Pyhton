def insertionSort(arr):
    for i in range(1, len(arr)):
        key= arr[i]
        j=i-1
        while  j>= 0 and arr[j] >key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
# Usage:
elements = [9, 7, 5, 6, 7, 2]
insertionSort(elements)
print(elements)  # Output: [2, 5, 6, 7, 7, 9]