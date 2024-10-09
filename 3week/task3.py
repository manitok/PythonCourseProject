class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        result = []
        
        def backtrack(start, target, current):
            if target == 0: 
                result.append(list(current))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue 
                if candidates[i] > target:
                    break 
                current.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current) 
                current.pop() 
        
        backtrack(0, target, [])
        return result