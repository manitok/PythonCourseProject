"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        ans = []
        window_substring = Counter(p)
        window = len(p)
        for i in range(len(s)-window+1):
            subs = Counter(s[i : window+i])
            if subs == window_substring:
                ans.append(start)
            subs[s[i]]-=1
            if subs[s[i]]==0:
                del subs[s[i]]
            start+=1
        return ans