import collections

class Solution:
    def sumOfPerfectSquarePairs(self, n: int, edges: list[list[int]], nums: list[int]) -> int:
        
        MAX_VAL = 100001
        spf = list(range(MAX_VAL))
        for i in range(2, int(MAX_VAL**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, MAX_VAL, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_square_free_part(num):
            sf = 1
            while num > 1:
                p = spf[num]
                count = 0
                while num % p == 0:
                    num //= p
                    count += 1
                if count % 2 == 1:
                    sf *= p
            return sf

        sf_nums = [get_square_free_part(num) for num in nums]

        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.total_pairs = 0
        path_counts = collections.defaultdict(int)

        def dfs(u, parent):
            my_sf = sf_nums[u]
            
            ancestor_matches = path_counts[my_sf]
            
            if u != 0:
                self.total_pairs += ancestor_matches
            
            path_counts[my_sf] += 1
            
            for v in adj[u]:
                if v != parent:
                    dfs(v, u)
            
            path_counts[my_sf] -= 1

        dfs(0, -1)
        
        return self.total_pairs