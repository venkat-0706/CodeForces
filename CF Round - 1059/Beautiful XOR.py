import sys

class Transformer:
    def solve(self):
        try:
            a, b = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            return

        if a == b:
            print(0)
            print()
            return

        a_bl = a.bit_length()
        b_bl = b.bit_length()

        if a_bl < b_bl:
            print(-1)
            return

        if a_bl == b_bl:
            x = a ^ b
            print(1)
            print(x)
            return

        if a_bl > b_bl:
            k = a_bl - 1
            l = b_bl - 1
            
            c = (1 << k) | (1 << l)
            
            x1 = a ^ c
            x2 = c ^ b
            
            print(2)
            print(x1, x2)

def main():
    try:
        t = int(sys.stdin.readline())
        solver = Transformer()
        for _ in range(t):
            solver.solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()