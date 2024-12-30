class Solution:
    def getSecondLargest(self, arr):
        largest = 0
        secondLargest = 0
        noSecondLargest = -1
        sortedArr = sorted(arr)

        for i in sortedArr:
            if largest < i:
                secondLargest = largest
                largest = i 
        return secondLargest if secondLargest != 0 else noSecondLargest
      


solution = Solution()
arr = [12, 35, 1, 10, 34, 1]
print(solution.getSecondLargest(arr))