class Solution:
    def trimZero(self,s):
        return s[s.find('1'):]

    def addBinary(self, s1, s2):
            s1 = self.trimZero(s1)
            s2 = self.trimZero(s2)
            
            n = len(s1)
            m = len(s2)
            
            carry =0
            
            result = []
            
            if n<m:
                s1, s2 = s2 , s1
                n, m = m, n
                
            j = m-1
            
            for i in range(n-1,-1,-1):
                bit1 = int(s1[i])
                bitSum = bit1+carry
                
                if j>=0:
                    bit2 = int(s2[j])
                    bitSum+=bit2
                    
                    j-=1
                    
                bit = bitSum%2
                carry = bitSum//2
                
                result.append(str(bit))
                
            if carry > 0:
             result.append("1")
                
            return ''.join(result[::-1])
        
        
        

	    
	    

s =Solution()
s1 = "001010"
s2 = "0111"

print(s.addBinary(s1,s2))