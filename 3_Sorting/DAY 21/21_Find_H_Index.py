class Solution:
    def hIndex(citations):
        n = len(citations)
        freq = [0] * (n + 1)
        for citation in citations:
            if citation >= n:
                freq[n] += 1
            else:
                freq[citation] += 1

        idx = n
        
        s = freq[n]
        while s < idx:
            idx -= 1
            s += freq[idx]
        return idx

citations = [6, 0, 3, 5, 3]
s = Solution()
print(s.hIndex(citations))