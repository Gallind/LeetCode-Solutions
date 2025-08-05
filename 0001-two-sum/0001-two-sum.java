class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int[] sol_indices = new int[2];
        for (int i = 0; i < n; i++){
            //if (nums[i] > target) continue;
            for (int j = i+1; j < n; j++){
                if (nums[i] + nums[j] == target){
                    sol_indices[0] = i;
                    sol_indices[1] = j;
                    return sol_indices;
                }
            }
        }
        return sol_indices;
    }
}