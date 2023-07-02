def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        # Find the minimum element in the unsorted portion
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the minimum element with the leftmost element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Usage:
elements = [9, 7, 5, 6, 7, 2]
selectionSort(elements)
print(elements)  # Output: [2, 5, 6, 7, 7, 9]
