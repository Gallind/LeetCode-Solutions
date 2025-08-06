class Solution {
    public int majorityElement(int[] nums) {
        int curr = nums[0];
        int count = 0;
        for (int num : nums){
            if (count == 0){
                count++;
                curr = num;
            }
            else{
                if (num == curr) count++;
                else count--;
            }
        }
        return curr;
    }
}