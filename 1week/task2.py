class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        output = ""
        for i in range(len(words)):
            output += words[len(words) - 1 - i] + " "
        return output[:-1]
