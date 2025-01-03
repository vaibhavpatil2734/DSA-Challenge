class Solution:
    def myAtoi(self, s : str)->int:
        index =0
        res =0
        sign =1
        max = 2**31-1
        min = -2**31
        
        while index<len(s) and s[index]==' ':
            index+=1
            
        if index<len(s) and (s[index]=='+' or s[index]=='-'):
            if s[index]=='-':
                sign=-1
            index+=1
            
        if res>(2**31-1):
            return sign*(2**31-1)if sign==1 else -2**31
            
        while index<len(s) and '0'<=s[index]<='9':
            digit = ord(s[index])-ord('0')
            if res>(max - digit)//10:
                return max if sign ==1 else min
            res=res*10+digit
            index+=1
        
        
            
        return res*sign
        
        if res == 0:
            return 0




S1 = Solution()
s = "12345"
print(S1.myAtoi(s))