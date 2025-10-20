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
                nk_line = sys.stdin.readline()
                if not nk_line:
                    continue
                n, k = map(int, nk_line.split())
                s = sys.stdin.readline().strip()
                if not s:
                    continue
                
                ans = 0
                last_protected_one = -k 
                
                for i in range(n):
                    if s[i] == '1':
                        if i - last_protected_one >= k:
                            ans += 1
                            last_protected_one = i
                        else:
                            last_protected_one = i
                            
                results.append(str(ans))
            
            print('\n'.join(results))
        except EOFError:
            pass
        except Exception as e:
            pass

if __name__ == "__main__":
    solver = Solution()
    solver.solve_test_cases()