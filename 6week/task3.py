"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)

        return len(s)