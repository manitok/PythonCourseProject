class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = len(nums) - 1

            while low < high:
                curr_sum = nums[i] + nums[low] + nums[high]
                
                if curr_sum < 0:
                    low += 1
                elif curr_sum > 0:
                    high -= 1

                else:
                    triplets.append([nums[i], nums[low], nums[high]])

                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    
                    low += 1
                    high -= 1
        
        return triplets
            