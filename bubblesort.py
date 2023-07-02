def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                print(arr)
elements= [9,7,5,6,7,2]
bubbleSort(elements)

print("sorted Array")
print(elements)