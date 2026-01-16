class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        for i, num in enumerate(nums):
            if num not in indices:
                indices[num] = {i,}
            else:
                for index in indices[num]:
                    if i - index <= k: return True
                indices[num].add(i)
        return False