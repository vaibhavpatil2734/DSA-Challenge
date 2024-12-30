class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        maxProd = float('-inf')  # Initialize to negative infinity
    
        leftToRight = 1
        rightToLeft = 1
    
        for i in range(n):
            # Reset the product to 1 if it becomes 0
            if leftToRight == 0:
                leftToRight = 1
            if rightToLeft == 0:
                rightToLeft = 1
        
            # Multiply elements from left to right
            leftToRight *= arr[i]
        
            # Multiply elements from right to left
            j = n - i - 1
            rightToLeft *= arr[j]
            
            # Update maxProd with the maximum of leftToRight, rightToLeft, or maxProd
            maxProd = max(leftToRight, rightToLeft, maxProd)
        
        return maxProd


# Test the solution
s = Solution()
arr = [-2, 6, -3, -10, 0, 2]
print(s.maxProduct(arr))  # Expected output: 180
