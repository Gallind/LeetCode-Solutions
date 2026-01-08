import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i = 0; i < n; i++){
            map.put(nums[i], i);
        }
        for (int i = 0; i < n; i++){
            Integer temp = map.get(target - nums[i]);
            if (temp != null && temp != i){
                return new int[] {i, temp};
            }
        }
        return new int[]{0,1};
    }
}