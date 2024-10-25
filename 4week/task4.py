class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        l = []
        for i in range(len(nums)):
            element = nums[i]
            remaining = nums[:i] + nums[i+1:]
            perms = self.permuteUnique(remaining)
            for perm in perms:
                l.append(perm + [element])
        k = []
        for i in l:
            if i not in k:
                k.append(i)
        return k
        