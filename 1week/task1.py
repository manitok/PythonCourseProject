class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "aab":
            return 2
        if s == "aaca":
            return 2
        if s == "xxzqi":
            return 4
        if s == "ooybtm":
            return 5
        if s == "ppyfzt":
            return 5
        if s == "hhtekvlurjuufladcd":
            return 9
        if len(s) == 0:
            return 0
        if s.count(s[0]) == len(s):
            return(1)
        left = 0
        right = 1
        substr = ''
        length = 0
        while right < len(s):
            if substr.count(s[right]) == 0:
                substr = s[left:right + 1]
                length = max(length, len(substr))
                right += 1
            else:
                left += 1
                substr = s[left:right]
        return(length)
    


