class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        int n = nums.length;
        if (n == 0) return 0;
        int max = nums[n - 1];
        int curr = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++){
            if (curr == max) break;
            if (curr == nums[i]) continue;
            nums[k++] = nums[i];
            curr = nums[i];
        }
        return k;
    }
}