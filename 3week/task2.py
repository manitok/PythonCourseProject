class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []

        def backtracking(index: int, comb: list[int], total: int):
            if total == target:
                ans.append(comb[:])
                return

            for i in range(index, len(candidates)):
                newTotal = total + candidates[i]

                if newTotal > target:
                    return

                comb.append(candidates[i])
                backtracking(i, comb, newTotal)
                comb.pop()

        backtracking(0, [], 0)
        return ans