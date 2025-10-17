import sys

def solve():
    try:
        n, m = map(int, sys.stdin.readline().split())
        min_len = n + 1 
        for _ in range(m):
            l, r = map(int, sys.stdin.readline().split())
            length = r - l + 1
            if length < min_len:
                min_len = length
    except (IOError, ValueError):
        return

    result = [str(i % min_len) for i in range(n)]
    

    print(" ".join(result))

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
        for _ in range(t):
            solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()