MOD = 998244353

class RiffleShuffle:
    def solve(self):
        import sys
        input = sys.stdin.readline

        t = int(input())
        for _ in range(t):
            n = int(input())
            p = list(map(int, input().split()))

            missing = [1] * (n + 1)
            for x in p:
                if x != -1:
                    missing[x] = 0

            pre = [0] * (n + 1)
            for i in range(1, n + 1):
                pre[i] = pre[i - 1] + missing[i]

            dp = [[0] * (n + 1) for _ in range(n + 1)]
            dp[0][0] = 1

            for i in range(1, n + 1):
                for k in range(0, i):
                    if dp[i - 1][k] == 0:
                        continue
                    if p[i - 1] != -1:
                        if p[i - 1] <= k:
                            dp[i][k] = (dp[i][k] + dp[i - 1][k]) % MOD
                        if p[i - 1] > k:
                            dp[i][k + 1] = (dp[i][k + 1] + dp[i - 1][k]) % MOD
                    else:
                        cnt_low = k - (pre[n] - pre[k])
                        cnt_high = (pre[n] - pre[k]) - (i - 1 - k - (p[:i - 1].count(-1) - (pre[n] - pre[i - 1])))

                        if cnt_low > 0:
                            dp[i][k] = (dp[i][k] + dp[i - 1][k] * cnt_low) % MOD
                        if cnt_high > 0:
                            dp[i][k + 1] = (dp[i][k + 1] + dp[i - 1][k] * cnt_high) % MOD

            print(sum(dp[n]) % MOD)


if __name__ == "__main__":
    RiffleShuffle().solve()
