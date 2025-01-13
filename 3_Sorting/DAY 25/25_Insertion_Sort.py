def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1
        print(j)


        while j >= 0 and arr[j] > key:
            print(f"Shifting {arr[j]} to position {j + 1}")
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Inserting {key} at position {j + 1}")
        print("Array after this step:", arr)

    return arr

if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("Original array:", data)
    sorted_array = insertion_sort(data)
    print("Sorted array:", sorted_array)
