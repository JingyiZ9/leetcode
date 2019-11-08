Solution 1: use hashmap
遍历数组，未访问过的数字左右扩张，得到连续长度，与maxVal比较
最后更新该数字的最大连续长度，然后更新左右边界值

```
class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int res = 0;
        for (int i=0; i<nums.length; i++) {
            if (!map.containsKey(nums[i])) {
                int left = (map.containsKey(nums[i]-1)) ? map.get(nums[i]-1) :0;
                int right = (map.containsKey(nums[i]+1)) ? map.get(nums[i]+1):0;
                int sum = left+right+1;
                res = Math.max(res,sum);
                // update the boundary for nums[i];
                map.put(nums[i], sum);
                map.put(nums[i]-left, sum);
                map.put(nums[i]+right, sum);
            }
            else
                continue;
        }
        return res;
    }
}
```

Solution2: Set
访问过的数字从set中移除，同时与之相连的数字均可移除，减少检查次数

```
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums==null || nums.length==0) return 0;
        Set<Integer> set = new HashSet<Integer>();
        int res = 1;
        for (int i=0; i<nums.length; i++) set.add(nums[i]);
        
        for (int num:nums) {
            if (set.remove(num)) { //num has not been visited
                int val = num;
                int sum = 1;
                while (set.remove(val-1)) val--;
                sum += num-val;
                val = num;
                while (set.remove(val+1)) val++;
                sum += val-num;
                res = Math.max(res,sum);
            }
        }
        return res;
    }
}
```