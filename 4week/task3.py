class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 

        nums.sort() 
        longest = 0
        curr_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr_length += 1
            elif nums[i] != nums[i-1]:
                longest = max(longest, curr_length)
                curr_length = 1

        return max(longest, curr_length)