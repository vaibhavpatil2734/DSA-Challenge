class Solution:
    def pushZerosToEnd(self,arr):
        
        newArr = []
        zeroCount = 0
        for i in range(len(arr)):
            if arr[i] != 0 :
                newArr.append(arr[i])
            else:
                zeroCount = zeroCount+1
        while zeroCount!=0:
            newArr.append(0)
            zeroCount=zeroCount-1
        return newArr   


s = Solution()
arr = [12,0,34,0,0,2,3]
print(s.pushZerosToEnd(arr))