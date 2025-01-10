def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swaped = False
        print("pass",i)
        for j in range(len(arr)-1-i):
            
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] 
                swaped = True
        if not swaped:
            break
       
    return arr  

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print("Sorted Array:", sorted_arr)
