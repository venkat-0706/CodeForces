class Solution:
    def maxAverageSubarray(self, arr):
        return max(arr)

if __name__ == "__main__":
    t = int(input().strip())
    sol = Solution()
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        print(sol.maxAverageSubarray(arr))
