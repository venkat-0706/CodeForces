import sys

class Solution:
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
                
                if n % 2 == 0:
                    results.append("0")
                    continue
                
                total_cost = 0
                for i in range(1, n - 1, 2):
                    peak_val = max(a[i-1], a[i+1])
                    if a[i] <= peak_val:
                        total_cost += (peak_val + 1 - a[i])
                
                results.append(str(total_cost))
            
            print('\n'.join(results))
        except EOFError:
            pass
        except Exception as e:
            pass

if __name__ == "__main__":
    solver = Solution()
    solver.solve_test_cases()