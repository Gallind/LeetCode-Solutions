import math
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 3: return False

        smallest = math.inf
        second = math.inf #infinity, not infimum

        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= second:
                second = n
            else: return True
        
        return False








        # i, j, k = 0, 1, 2
        # vi, vj, vk = nums[i], nums[j], nums[k]
        # while vi >= vj:
        #     i += 1
        #     j += 1
        #     k += 1
        #     if k >=l : return False
        #     vi, vj, vk = nums[i], nums[j], nums[k]
        # while vj >= vk:
        #     k += 1
        #     if k >= l: return False
        #     vk = nums[k]
        # return True