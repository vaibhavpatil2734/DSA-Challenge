class Solution:
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        n = len(arr)
        maxSum = arr[0]  # Initialize to the first element
        currentSum = 0
        
        for i in range(n):
            currentSum += arr[i]
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:  # Reset currentSum if it drops below 0
                currentSum = 0
                
        return maxSum

if __name__ == "__main__":
    s = Solution()
    arr = [2, 3, -8, 7, -1, 2, 3] 
    print("Maximum Subarray Sum:", s.maxSubArraySum(arr))  # Print the result
