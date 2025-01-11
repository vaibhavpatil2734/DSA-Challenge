def selection_sort(arr):
    n = len(arr)-1
    small = 0
    for i in range(n):
        
        for j in range(i+1,len(arr)):
            if(arr[small]>arr[j]):
                small = j
        arr[i] ,arr[small] = arr[small],arr[i]
        small = i+1
    return arr 
                
    

# Example Usage
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original array:", data)
    print("sorted array:",selection_sort(data))
