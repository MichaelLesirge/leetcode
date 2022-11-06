# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        """
        assign min val to each index
        exsplore all possiblities and cache index values

        reminds me of fibonacci sequance 
        """
        memo = {}

        end_at = len(costs)-2

        def minCostForStair(i=-1):
            if i not in memo:
                memo[i] = costs[i] if i != -1 else 0
                if i < end_at:
                    memo[i] += min(minCostForStair(i+1), minCostForStair(i+2))
            return memo[i]

        return minCostForStair()
