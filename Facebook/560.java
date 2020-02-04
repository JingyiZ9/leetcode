// subarray equals to K
//solution 1: prefix[j] - prefix[i] == k
// O(n^2)

class Solution {
    public int subarraySum(int[] nums, int k) {
        // prefix sum
        int res = 0;
        int[] pre_sum = new int[nums.length+1];
        pre_sum[0] = 0;
        
        for (int i=1; i<=nums.length; i++) {
            pre_sum[i] = pre_sum[i-1] + nums[i-1];
        }
        
        for (int i=0; i<nums.length; i++) {
            for (int j=i; j<nums.length; j++) {
                if (pre_sum[j+1] - pre_sum[i] == k)
                    res++;
            }
        }
        
        return res;
    }
}


// solution2: prefix + hashtable
// O(N)

class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        int pre_sum = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0,1);
        
        for (int num:nums) {
            pre_sum += num;
            if (map.containsKey(pre_sum-k))
                res += map.get(pre_sum-k);
            if (map.containsKey(pre_sum))
                map.put(pre_sum, map.get(pre_sum)+1);
            else
                map.put(pre_sum, 1);
        }
        return res;
    }
}