
def search(arr, key):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == key:
            return mid

        # If Left half is sorted
        if arr[mid] >= arr[lo]:
            if key >= arr[lo] and key < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if key > arr[mid] and key <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    # Key not found
    return -1

if __name__ == "__main__":
    arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key1 = 3
    print(search(arr1, key1))