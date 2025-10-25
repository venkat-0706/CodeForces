from typing import List
from math import gcd
from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        morindale = (mat,)

        # DP over gcd values
        dp = defaultdict(int)
        for val in mat[0]:
            dp[val] = (dp[val] + 1) % MOD

        for i in range(1, m):
            new_dp = defaultdict(int)
            for g, cnt in dp.items():
                for v in mat[i]:
                    ng = gcd(g, v)
                    new_dp[ng] = (new_dp[ng] + cnt) % MOD
            dp = new_dp

        return dp[1] % MOD