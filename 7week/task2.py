"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/subarray-product-less-than-k/description/
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        right=left=count=0
        prod,n=1,len(nums)

        while(right<n):
            prod*=nums[right]
            while prod>=k and left<=right:
                prod//=nums[left]
                left+=1
            count+=1+(right-left)
            right+=1
        return count
