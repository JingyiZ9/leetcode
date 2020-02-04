class Solution {
    public String addBinary(String a, String b) {
        // edge cases
        if (a == null || a.length() == 0) return b;
        if (b == null || b.length() == 0) return a;
        
        int alen = a.length()-1;
        int blen = b.length()-1;
        int carry = 0;
        StringBuffer res = new StringBuffer("");
        
        while (alen>=0 || blen>=0 || carry ==1) {
            if (alen>=0) {
                carry += a.charAt(alen) - '0';
                alen--;
            }
            if (blen>=0) {
                carry += b.charAt(blen) - '0';
                blen--;
            }
            
            res.append((char) (carry%2 + '0'));
            carry = carry/2;
        }
        return res.reverse().toString();
    }
}