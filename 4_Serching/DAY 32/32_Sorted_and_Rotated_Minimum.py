def findMin(arr):
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        if arr[lo] < arr[hi]:
            return arr[lo]
      
        mid = (lo + hi) // 2
        if arr[mid] > arr[hi]:
            lo = mid + 1
          
        else:
            hi = mid

    return arr[lo]

if __name__ == "__main__":
    arr = [5, 6, 1, 2, 3, 4]
    print(findMin(arr))