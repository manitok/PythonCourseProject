"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
"""

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], L1: int, L2: int) -> int:
        if L1 < L2:
            L1, L2 = L2, L1
        N = len(nums)
        ps = [0]
        for num in nums:
            ps.append(ps[-1] + num)
        max_prefix = [0] * (N + 1)
        max_suffix = [0] * (N + 1)
        for i in range(N - L2):
            max_prefix[i] = max(max_prefix[i - 1], ps[i + 1] - ps[i - L2 + 1])
            i = N - L2 - i
            max_suffix[i] = max(max_suffix[i + 1], ps[i + L2] - ps[i])
        max_sum = 0
        for i in range(N - L1 + 1):
            max_sum = max(max_sum, ps[i + L1] - ps[i] + max(max_prefix[i - 1], max_suffix[i + L1]))
        return max_sum