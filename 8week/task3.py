"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/max-consecutive-ones-iii/description/
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        for i,num in enumerate(nums):
            k -= 1-num
            if k < 0:
                k += 1-nums[l]
                l += 1
            else:
                res = max(res , i-l+1)
        return res