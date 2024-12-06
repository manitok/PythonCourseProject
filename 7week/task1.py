"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements/description/
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        l, r = 0, N - 1
        while l < r:
            mid = l + (r - l) // 2
            if mid + k < N and (x - arr[mid] > arr[mid + k] - x):
                l = mid + 1
            else:
                r = mid
        return arr[r:r + k]
    
        N = len(arr)
        j = 0
        ans = []
        for i in range(N - k + 1):
            while j < N and j - i < k:
                ans.append(arr[j])
                j += 1
            if j == N or (abs(arr[j] - x) > abs(arr[i] - x)) or ((abs(arr[j] - x) == abs(arr[i] - x)) and arr[j] > arr[i]):
                return ans
            ans.pop(0)
        return ans
            