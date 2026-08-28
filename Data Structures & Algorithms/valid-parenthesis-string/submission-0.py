class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min  =0 
        left_max = 0
        for c in s:
            if c == '(':
                left_min += 1
                left_max += 1
            elif c == ')':
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            if left_max < 0:
                return False
            left_min = max(0, left_min)
        return left_min == 0