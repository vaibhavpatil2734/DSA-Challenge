class Solution:
    
    def reverseArray(self, arr):
        left = 0 
        right = len(arr)-1
        while left < right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
        
        
        
s = Solution()
arr = [12,0,34,0,0,2,3]
print(s.reverseArray(arr))