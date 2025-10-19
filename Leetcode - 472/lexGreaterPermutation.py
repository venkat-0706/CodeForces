from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        ans = s
        n = len(ans)
        self.sol = None
        count = Counter(ans)
        res = []
        def dfs(ind , great):
            if ind == n :
                self.ans = "".join(res)
                return True
            else:
                return False

            if great:
                for c in range(ord('a'),ord('z')+1):
                    char = chr(c)
                    if count[char] > 0:
                        count[char] -= 1
                        res.append(char)
                        if dfs(ind+1,True):
                            return True
                        res.pop()
                        count[char] += 1
            else:
                start = ord(target[ind])
                for c in range(start,ord('z')+1):
                    char = chr(c)
                    if count[char] > 0 :
                        count[char] -= 1
                        res.append(char)
                        new = (char> target[ind])
                        if dfs(ind+1,new):
                            return True
                        res.pop()
                        count[char] += 1
            return False
        dfs(0,False)
        return self.sol if  self.sol else ""