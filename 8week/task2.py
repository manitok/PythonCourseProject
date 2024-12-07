"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/get-equal-substrings-within-budget/description
"""

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        comps = []
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                comps.append(1)
            elif arr[i] < arr[i+1]:
                comps.append(-1)
            else:
                comps.append(0)
        
        max_len = 0

        l = 0
        for r in range(len(comps)):
            # print(comps[r], l, r)
            if comps[r] == 0:
                max_len = max(max_len, r - l)
                l = r + 1
            elif (comps[r] == comps[l] and (r - l) % 2 == 1) or (comps[r] == -comps[l] and (r - l) % 2 == 0):
                max_len = max(max_len, r - l)
                l = r
        max_len = max(max_len, len(comps) - l)
        
        return max_len + 1

