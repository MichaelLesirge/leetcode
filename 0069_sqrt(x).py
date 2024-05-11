# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        # Minor optimization: square root has to be between these to numbers based on above check
        # without the extra check then left=0, right=x
        left = 1
        right = x // 2

        # pretty normal binary search
        while left <= right:
            mid = (left + right) // 2
            midSq = mid * mid
            if midSq > x:
                right = mid - 1
            elif midSq < x:
                left = mid + 1
            else:
                return mid
        
        return right
