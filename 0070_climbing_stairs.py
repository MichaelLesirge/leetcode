# https://leetcode.com/problems/climbing-stairs/

class Solution:
    # recursive + memo
    def climbStairsRecursive(self, n: int, memo={1: 1, 2: 2}) -> int:  # memo = {i: i for i in range(0, 4)}
        if n not in memo:
            memo[n] = self.climbStairsRecursive(n-1) + self.climbStairsRecursive(n-2)
        return memo[n]
        
