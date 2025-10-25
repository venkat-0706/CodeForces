class Solution:
    def lexSmallest(self, s: str) -> str:
        n  =len(s)
        best = None
        for k in range(1,n+1):
            res = s[:k][::-1] + s[k:]
            ans = s[:-k]+s[-k:][::-1] if k!=n else s[::-1]
            if best is None or res < best:
                best =  res
            if ans < best:
                best = ans
        return best