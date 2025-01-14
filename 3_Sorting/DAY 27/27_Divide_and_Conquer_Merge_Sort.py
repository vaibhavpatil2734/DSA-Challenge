def merge_sort(arr):
    # Base case: If the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Step 2: Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # Step 3: Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    # Compare elements from both arrays and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            print(left[i])
            result.append(left[i])
            i += 1
        else:
            print(right[j])
            result.append(right[j])
            j += 1
    
    # Append remaining elements from the left array
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Append remaining elements from the right array
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

# Example usage:
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 2, 5, 5, 6, 9]
