class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        pivot = -1

        # Step 1: Find the pivot index
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break

        # Step 2: If pivot doesn't exist, reverse the array
        if pivot == -1:
            arr.reverse()
            return

        # Step 3: Find the smallest number greater than pivot
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # Step 4: Reverse the elements to the right of the pivot
        left, right = pivot + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr


s = Solution()
arr = [2, 4, 1, 7, 5, 0]
print(s.nextPermutation(arr))
