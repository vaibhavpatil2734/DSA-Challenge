#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        s1 =s1+s1
        
        if s2 in s1:
            return True
        else:
            return False
        
        
s = Solution()
s1 = "abcd"
s2 = "dabca"
print(s.areRotations(s1,s2))