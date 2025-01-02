class Solution:
    def myAtoi(self, s):
        index =0
        res =0
        sign = 1

        #To remove white space
        while index<len(s) and s[index] == " ":
            index+=1
        

        #To find sign 
        if index<len(s) and (s[index]=="+" or s[index]=='-'):
            if s[index]=='-':
                sign = -1
            index+=1

        #To check over and under flow
        if res > (2**31 - 1):
            return sign * (2**31 - 1) if sign == 1 else -2**31
        
        #To conver and store the int values
        while index<len(s):
            digit = ord(s[index])-ord('0')
            res = res*10+digit
            index+=1

        
        return res*sign

        





S1 = Solution()
s = "12345"
print(S1.myAtoi(s))