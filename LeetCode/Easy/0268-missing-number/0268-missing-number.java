class Solution {
    public int missingNumber(int[] nums) {
        int max = -1;
        int sum = 0;
        for (int num : nums){
            if (num > max) max = num;
            sum += num;
        }
        int n = nums.length;
        if (max < n) return n;
        int fullSum = (int)((n * (n + 1))/2);
        return fullSum - sum;
    }
}