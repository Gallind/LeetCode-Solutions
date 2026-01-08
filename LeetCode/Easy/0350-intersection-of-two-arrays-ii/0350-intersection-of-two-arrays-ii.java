class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        ArrayList<Integer> inter = new ArrayList<>();
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int[] count1 = new int[nums1[nums1.length - 1] + 1];
        int[] count2 = new int[nums2[nums2.length - 1] + 1];
        for (int i = 0; i < count1.length; i++){
            count1[i] = 0;
        }
        for (int i = 0; i < count2.length; i++){
            count2[i] = 0;
        }
        for (int num : nums1) count1[num]++;
        for (int num : nums2) count2[num]++;

        int rep = -1;
        if (nums1[nums1.length-1] <= nums2[nums2.length-1]){
            for (int num : nums1){
                if (num == rep) continue;
                rep = num;
                int min = Math.min(count1[num], count2[num]);
                for (int i = 0; i < min; i++){
                    inter.add(num);
                    count2[num]--;
                }
            }
        }
        else{
            for (int num : nums2){
                if (num == rep) continue;
                rep = num;
                int min = Math.min(count1[num], count2[num]);
                for (int i = 0; i < min; i++){
                    inter.add(num);
                    count1[num]--;
                }
            }
        }
        int[] output = new int[inter.size()];
        for (int i = 0; i < inter.size(); i++){
            output[i] = inter.get(i);
        }
        return output;
    }
}