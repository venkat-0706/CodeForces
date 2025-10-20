import sys
import threading
def main():
    import bisect
    t = int(sys.stdin.readline())
    class Solver:
        def solve(self, n, k, a):
            a.sort(reverse=True)
            res = sum(a)
            best = res
            for x in range(1, min(n, 2*k+1) + 1, 2):
                cur = 0
                ops = k
                idx = 0
                while ops >= 0 and idx < n:
                    cur += a[idx]
                    idx += x
                    ops -= 1
                best = max(best, cur + sum(a[idx:]))
            return best
    obj = Solver()
    out = []
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        out.append(str(obj.solve(n, k, a)))
    print("\n".join(out))
threading.Thread(target=main).start()
