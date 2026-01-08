class Solution {
    public int searchInsert(int[] nums, int target) {
        return binarySearch(nums, 0, nums.length - 1, target);
    }
    private int binarySearch(int[] nums, int l, int r, int target){
        int m = (int) ((r + l) / 2);
        if (l - r >= 0){
            return nums[m] < target ? m+1 : m;
        }
        if (nums[m] == target) return m;
        if (nums[m] > target) return binarySearch(nums, l, m - 1, target);
        if (nums[m] < target) return binarySearch(nums, m + 1, r, target);
        return -1;
    }
}