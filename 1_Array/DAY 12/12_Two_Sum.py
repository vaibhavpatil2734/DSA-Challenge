class Solution(object):
    def twoSum(self, nums, target):
        n =len(nums)-1
        j=1
        res=[]
        for i in range(n):
            
            if nums[i]+nums[j]==target:
                res.append(i)
                res.append(j)
            if j >= n:
                break
            else:
                j+=1
            
        return res


s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums,target))

#leetcode