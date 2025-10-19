from typing import List
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        curr = k
        while curr in nums:
            curr += k
        return curr