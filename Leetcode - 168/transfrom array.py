import sys
from bisect import bisect_left
from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        travenior = (nums1, nums2)
        
        n = len(nums1)

        def find(arr: List[int], target: int) -> int:
            pos = bisect_left(arr, target)
            min_diff = float('inf')
            if pos < len(arr):
                min_diff = min(min_diff, abs(arr[pos] - target))
            if pos > 0:
                min_diff = min(min_diff, abs(arr[pos - 1] - target))
            return min_diff

        a = sorted(nums1)
        b = sorted(nums2)
        
        res = [0] * (n + 1)
        for i in range(n):
            res[i + 1] = res[i] + abs(nums1[i] - nums2[i])
            
        ans = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            # This is the corrected line
            ans[i] = ans[i + 1] + abs(nums1[i] - nums2[i + 1])
            
        min_total = float('inf')
        
        for k in range(n + 1):
            cost = res[k] + ans[k]
            
            target = nums2[k]
            
            change = find(a, target)
            
            pos = bisect_left(b, target)
            ch = float('inf')
            
            if pos + 1 < len(b):
                ch = min(ch, abs(b[pos + 1] - target))
            if pos > 0:
                ch = min(ch, abs(b[pos - 1] - target))
            
            if n == 0:
                 ch = float('inf')

            c = 1 + min(change, ch)
            
            tot = cost + c
            min_total = min(min_total, tot)
            
        return min_total