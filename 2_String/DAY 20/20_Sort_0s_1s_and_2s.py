class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        
        l = 0
        m = 0
        h = len(arr)-1
        
        while(m<=h):
                
            if(arr[m]==0):
                arr[l] , arr[m]= arr[m] , arr[l]
                l+=1
                m+=1
            if(arr[m]==2):
                arr[m] , arr[h] = arr[h] , arr[m]
                h-=1
        return arr    
        

s = Solution()
arr = [0, 1, 2, 0, 1, 2]
print(s.sort012(arr))
        

