def simple_merge_sort(arr, arr2):
    n = len(arr2)
    m = len(arr)
    arr3 = []
    i = j = 0

    # Merge the two arrays
    while i < m and j < n:
        if arr[i] < arr2[j]:
            arr3.append(arr[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    # Append remaining elements from either array
    if i < m:
        arr3.extend(arr[i:])
    if j < n:
        arr3.extend(arr2[j:])

    return arr3

if __name__ == "__main__":
    data = [1, 4, 7, 12]
    data2 = [2, 3, 5, 10, 25]
    sorted_array = simple_merge_sort(data, data2)
    print("Sorted array:", sorted_array)
