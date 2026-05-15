class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = nums
        for i in range(len(nums) - 1):
            self.pre_sum[i+1] += self.pre_sum[i]

    def sumRange(self, left: int, right: int) -> int:
        if not left: 
            return self.pre_sum[right]
        return self.pre_sum[right] - self.pre_sum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)