class Solution {
    public int reverse(int x) {
        int res = 0;
        int temp = 0;
        
        if (x < Integer.MIN_VALUE || x > Integer.MAX_VALUE) return 0;
        
        int flag = 0;
        
        if (x < 0) {
            flag = 1;
            x = -x;
        }
        
        while (x > 0) {
            temp = temp*10 + x%10;
            // if overload -> overflow
            if ((temp - x%10) /10 != res) return 0;
            res = temp;
            x /= 10;
        }
        
        if (flag == 1)
            res = -res;
        
        return res;
    }
}