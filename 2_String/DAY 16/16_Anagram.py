def areAnagrams(s1, s2):
    
    char = {}
    for c in s1:
        char[c]=char.get(c,0)+1
        
    for c in s2:
        char[c]=char.get(c,0)-1
        
    for c in char:
        if char[c] !=0:
            return False
        
    return True
        
        
        
s1="geeks"
s2="kseeg"
print(areAnagrams(s1,s2))