class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:
            return  ""
        if sum ==0:
            return ""
        dev = (num,sum)
        num_digits = dev[0]
        rem = dev[1]
        res = []
        for _ in range(num_digits):
            if rem >=9:
                res.append('9')
                rem -= 9
            elif rem > 0:
                res.append(str(rem))
                rem = 0
            else:
                res.append('0')
        return "".join(res)