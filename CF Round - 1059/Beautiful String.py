import sys

class SubsequenceSolver:
    def solve_case(self):
        try:
            n = int(sys.stdin.readline())
            s = sys.stdin.readline().strip()
        except (IOError, ValueError):
            return

        for mask in range(1 << n):
            p = []
            p_indices = []
            x = []

            for i in range(n):
                if (mask >> i) & 1:
                    p.append(s[i])
                    p_indices.append(i + 1)
                else:
                    x.append(s[i])

            is_p_non_decreasing = True
            for i in range(len(p) - 1):
                if p[i] > p[i + 1]:
                    is_p_non_decreasing = False
                    break
            
            if not is_p_non_decreasing:
                continue

            is_x_palindrome = (x == x[::-1])

            if is_x_palindrome:
                print(len(p_indices))
                print(*p_indices)
                return
                
        print(-1)

def main():
    try:
        t = int(sys.stdin.readline())
        solver = SubsequenceSolver()
        for _ in range(t):
            solver.solve_case()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()