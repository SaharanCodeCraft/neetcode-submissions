class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmin = 1
        curmax = 1
        for n in nums:
            if n == 0:
                curmin = 1
                curmax = 1
                continue
            temp = curmax
            curmax = max( n* curmax, n*curmin, n)
            curmin = min(n*temp, n*curmin, n)
            res = max(res, curmax)
        return res