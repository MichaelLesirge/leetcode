# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:  # only find first
                length = 1

                while num + length in nums:
                    length += 1
                
                if length > longest:
                    longest = length

        return longest
