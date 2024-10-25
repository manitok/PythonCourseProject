def isInInterval(start,end,target):
        if target >= start and target<=end:
            return True
        return False
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(intervals, key=lambda x: (x[0], x[1]))
        ans = []
        for ind,item in enumerate(sorted_list):
            if len(ans) == 0:
                ans.append(item)
                continue
            else:
                last_item = ans[len(ans) - 1]
                if isInInterval(last_item[0],last_item[1],item[0]):
                    #Overlap
                    ans[len(ans)-1][1] = max(ans[len(ans)-1][1],item[1])
                else:
                    ans.append(item)
        return ans
                