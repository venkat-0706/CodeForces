from typing import List
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = nums
        n = len(res)
        max_len = 0 
        for i in range(n):
            even = set()
            odd = set()
            for j in range(i,n):
                num = res[j]
                if num%2==0:
                    even.add(num)
                else:
                    odd.add(num)
                pos1 = len(even)
                pos2 = len(odd)
                if pos1 == pos2:
                    max_len = max(max_len ,j-i+1)

                rem = n-1-j
                if abs(pos1-pos2) > rem:
                    break

        return max_len