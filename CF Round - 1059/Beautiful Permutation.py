import sys

class InteractiveSolver:
    def ask(self, type_q, l, r):
        print(f"{type_q} {l} {r}", flush=True)
        response = sys.stdin.readline().strip()
        if not response:
            sys.exit()
        return int(response)

    def get_diff(self, l, r):
        if l > r:
            return 0
        sum_p = self.ask(1, l, r)
        sum_a = self.ask(2, l, r)
        return sum_a - sum_p

    def solve_case(self):
        n_str = sys.stdin.readline().strip()
        if not n_str:
            return
        n = int(n_str)
        
        total_diff = self.get_diff(1, n)
        L = total_diff

        low = 1
        high = n
        r = n 
        
        while low <= high:
            mid = low + (high - low) // 2
            
            diff_mid = self.get_diff(1, mid)
            
            if diff_mid == L:
                r = mid
                high = mid - 1
            else:
                low = mid + 1
        
        l = r - L + 1

        print(f"! {l} {r}", flush=True)

def main():
    try:
        t_str = sys.stdin.readline().strip()
        if not t_str:
            return
        t = int(t_str)
        
        solver = InteractiveSolver()
        for _ in range(t):
            solver.solve_case()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()