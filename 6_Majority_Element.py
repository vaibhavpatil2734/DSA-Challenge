class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        count1 =0
        count2=0
        ele1 =-1
        ele2 =-1
        for i in arr:
            
            if(ele1 == arr[i]):
                count1+=1
            elif(count1 == 0):
                ele1 = arr[i]
                count1 +=1
            elif(count2 == 0):
                ele2 = arr[i]
                count2 +=1
            elif(ele2 == arr[i]):
                count2+=1
            else:
                count1-=1
                count2-=1

        count1=0
        count2=0   
        res = []
        for i in arr:
            if ele1 == arr[i]:
                count1+=1
            if ele2 == arr[i]:
                count2+=1
        
        if count1>n/3:
            res.append(ele1)
        if count2>n/3:
            res.append(ele2)
            
        if res[0]>res[1]:
            res[0],res[1] = res[1],res[0]
    
        return res





s = Solution()
arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
print(s.findMajority(arr))