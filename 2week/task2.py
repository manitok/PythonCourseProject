class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        if len(num) == k + 1:
            return min(num)
        stack = []
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        ans = "".join(stack)
        ans = ans.lstrip("0")
        if ans == "":
            return "0"
        return ans
