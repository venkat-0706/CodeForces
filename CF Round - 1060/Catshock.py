import sys

class Solution:
    
    def solve_test_cases(self):
        try:
            t_line = sys.stdin.readline()
            if not t_line:
                return
            t = int(t_line)
            
            all_results = []
            
            for _ in range(t):
                n_line = sys.stdin.readline()
                if not n_line:
                    continue
                n = int(n_line.strip())
                
                adj = [[] for _ in range(n + 1)]
                for _ in range(n - 1):
                    line = sys.stdin.readline()
                    if not line:
                        continue
                    u, v = map(int, line.split())
                    adj[u].append(v)
                    adj[v].append(u)
                
                parent = {}
                children = [[] for _ in range(n + 1)]
                
                def dfs(u, p):
                    parent[u] = p
                    for v in adj[u]:
                        if v != p:
                            children[u].append(v)
                            dfs(v, u)
                
                dfs(n, n) 
                
                instructions = []
                curr = 1
                
                while curr != n:
                    target = parent[curr]
                    wrong_neighbors = children[curr]
                    
                    if not wrong_neighbors:
                        instructions.append("1")
                    else:
                        for i in range(len(wrong_neighbors)):
                            w = wrong_neighbors[i]
                            instructions.append(f"2 {w}")
                            instructions.append("1")
                            if i < len(wrong_neighbors) - 1:
                                instructions.append("1")
                                
                    curr = target
                    
                all_results.append(str(len(instructions)))
                all_results.extend(instructions)
            
            print('\n'.join(all_results))
            
        except EOFError:
            pass
        except Exception as e:
            pass

if __name__ == "__main__":
    sys.setrecursionlimit(400005)
    solver = Solution()
    solver.solve_test_cases()