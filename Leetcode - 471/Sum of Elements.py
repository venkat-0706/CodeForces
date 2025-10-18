from collections import Counter
from typing import List
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0 
        for val , ans in freq.items():
            if ans % k == 0:
                count += val * ans
        return count
        