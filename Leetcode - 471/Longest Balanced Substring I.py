class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len  = 0
        for i in range(n):
            freq = {}
            for j in range(i,n):
                freq[s[j]] = freq.get(s[j],0)+1
                values = list(freq.values())
                if len(set(values)) == 1:
                    max_len = max(max_len , j-i+1)
        return max_len