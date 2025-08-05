import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i = 0; i < n; i++){
            map.put(nums[i], i);
        }
        for (int i = 0; i < n; i++){
            int find = target - nums[i];
            if (map.get(find) != null && map.get(find) != i){
                return new int[] {i, map.get(find)};
            }
        }
        return new int[]{0,1};
    }
}