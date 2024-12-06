"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/new-21-game/description/
"""

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n >= k + maxPts:
            return 1
        prefix = [0] * (n + 2)
        prefix[1] = 1
        for i in range(1, n + 1):
            prefix[i + 1] = prefix[i] + (prefix[min(k - 1, i - 1) + 1] - prefix[max(0, i - maxPts)])/maxPts
        return prefix[n + 1] - prefix[k]
     
