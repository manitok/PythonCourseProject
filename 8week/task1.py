"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/get-equal-substrings-within-budget/description
"""

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        diff = []
        remCost = maxCost
        maxLen = 0

        for i in range(len(s)):
            diff.append(abs(ord(s[i])- ord(t[i])))
        
        i = 0
        j = 0

        while j < len(diff):
            remCost -= diff[j]
            if remCost >= 0:
                currLen = j - i + 1
                maxLen = max(currLen, maxLen)
                j += 1
            else:
                remCost += diff[i]
                i += 1
                j += 1
        return maxLen

        