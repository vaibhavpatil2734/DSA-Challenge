class Solution:
    
    def nonRepeatingChar(self,s):
        
        count = [-1]*26
        
        for i in range(len(s)):
            
            if count[ord(s[i])-ord('a')] == -1:
                count[ord(s[i])-ord('a')] = i
            else:
                count[ord(s[i]) - ord('a')] = -2
                
        idx = float('inf')
                
        for i in range(26):
            if count[i]>=0:
                idx = min(idx,count[i])
                
        return -1 if idx == float('inf') else s[idx]
    
s = Solution()
s1 = "abcaebc"
print(s.nonRepeatingChar(s1))
