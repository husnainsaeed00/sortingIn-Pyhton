def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def mergeSort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    mid_point = int(len(unsorted_list)/2)

    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]

    half_a = mergeSort(first_half)
    half_b = mergeSort(second_half)

    return merge(half_a, half_b)

if __name__ == '__main__':
    unsorted_list = [9, 5, 1, 8, 3, 6, 2, 7, 4]
    sorted_list = mergeSort(unsorted_list)
    print(sorted_list)
