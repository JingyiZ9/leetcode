// 返回**最少**运行task -> dp 或者贪心


class Solution {
    public int leastInterval(char[] tasks, int n) {
        //edge case
        if (n==0) return tasks.length;
        
        int[] dict = new int[26];
        
        for (char task:tasks) {
            dict[task-'A']++;
        }
        Arrays.sort(dict);
        int p = 24;
        
        while (dict[p] == dict[25]) {
            p--;
        }
        
        // calculate (n+1)*(max-1) + p
        int res = (dict[25]-1)*(n+1) + (25-p);
        
        return Math.max(res, tasks.length);
    }
}



