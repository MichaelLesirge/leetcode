# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        keep track of number of zeros
        for each element shift it over by the current number of zeros if its not zero
        replace end with number of zeros
        """
        num_of_zeros = 0
        for index, num in enumerate(nums):
            if num == 0:
                num_of_zeros += 1
            else:
                nums[index-num_of_zeros] = num
        
        for i in range(1, num_of_zeros+1):
            nums[-i] = 0
