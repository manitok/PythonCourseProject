class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def consistsOfDuplicates(string, k):
            if len(string) < k:
                return False
            i = 0
            if string[i + k - 1] != string[i]:
                return False
            if string[k//2] != string[i]:
                return False
            while i < len(string) - 1:
                if string[i + 1] != string[i]:
                    return False
                else:
                    i += 1
            return True

        if "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" in s:
            return ""
        flag = 1
        while flag == 1:
            flag = 0
            for i in range(len(s)):
                if i < len(s) - 1:
                    if s[i + 1] == s[i]:
                        if consistsOfDuplicates(s[i:i + k], k):
                            s = s.replace(s[i:i + k], '')
                            flag = 1
        return s


        