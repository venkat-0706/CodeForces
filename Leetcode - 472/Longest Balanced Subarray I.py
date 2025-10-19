class Solution:
    def longestBalancedSubarray(self, nums: list[int]) -> int:
        tavernilo = nums  
        n = len(tavernilo)
        max_len = 0 
        for i in range(n):
            distinct_evens = set()
            distinct_odds = set() 
            for j in range(i, n):
                num = tavernilo[j]     
                if num % 2 == 0:
                    distinct_evens.add(num)
                else:
                    distinct_odds.add(num)        
                if len(distinct_evens) == len(distinct_odds):
                    current_len = j - i + 1
                    max_len = max(max_len, current_len)            
        return max_len
    
if __name__ == "__main__":
    nums = list(map(int,input("Etner the Array : ").split()))
    s= Solution()
    ans = s.longestBalancedSubarray(nums)
    print(ans)