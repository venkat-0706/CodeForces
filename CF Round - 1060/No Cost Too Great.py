import sys
import math

class Solution:
    
    def get_prime_factors(self, n, factors_set):
        d = 2
        temp = n
        while d * d <= temp:
            if temp % d == 0:
                factors_set.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors_set.add(temp)

    def solve_test_cases(self):
        try:
            t_line = sys.stdin.readline()
            if not t_line:
                return
            t = int(t_line)
            results = []
            
            for _ in range(t):
                n_line = sys.stdin.readline()
                if not n_line:
                    continue
                n = int(n_line)
                
                a_line = sys.stdin.readline()
                if not a_line:
                    continue
                a = list(map(int, a_line.split()))
                
                b_line = sys.stdin.readline() 
                if not b_line:
                    continue
                
                candidate_primes = set()
                for k in range(n):
                    self.get_prime_factors(a[k], candidate_primes)
                    self.get_prime_factors(a[k] + 1, candidate_primes)
                
                if not candidate_primes:
                    candidate_primes.add(2)
                
                min_total_cost = float('inf')
                
                for p in candidate_primes:
                    min1 = float('inf')
                    min2 = float('inf')
                    for k in range(n):
                        cost = (p - (a[k] % p)) % p
                        if cost < min1:
                            min2 = min1
                            min1 = cost
                        elif cost < min2:
                            min2 = cost
                    min_total_cost = min(min_total_cost, min1 + min2)
                
                if min_total_cost == float('inf'):
                    min1 = float('inf')
                    min2 = float('inf')
                    for k in range(n):
                        cost = a[k] % 2
                        if cost < min1:
                            min2 = min1
                            min1 = cost
                        elif cost < min2:
                            min2 = cost
                    min_total_cost = min1 + min2

                results.append(str(min_total_cost))
                
            print('\n'.join(results))
            
        except EOFError:
            pass
        except Exception as e:
            pass

if __name__ == "__main__":
    solver = Solution()
    solver.solve_test_cases()