"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/grumpy-bookstore-owner/description/
"""

class Solution:
    def maxSatisfied(self, cust: List[int], grumpy: List[int], minutes: int) -> int:
        res = 0
        curr = 0
        for i in range(len(cust)):
            if grumpy[i] == 0:
                res += cust[i]
        for i in range(minutes):
            if grumpy[i] == 1:
                curr += cust[i]
        
        addi = curr  

        for i in range(minutes, len(cust)):
            if grumpy[i - minutes] == 1:
                curr -= cust[i - minutes]  
            if grumpy[i] == 1:
                curr += cust[i] 
            addi = max(addi, curr) 
        
        return res + addi  