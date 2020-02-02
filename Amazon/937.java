/* 排序日志文件
先按类型，数字在后，字母在前
再按字母顺序
字母顺序一样，按id顺序
*/





class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Comparator<String> myComp = new Comparator<>() {
            @Override
            public int compare(String str1, String str2) {
                int idx1 = str1.indexOf(" ");
                int idx2 = str2.indexOf(" ");
                
                String id1 = str1.substring(0,idx1);
                String id2 = str2.substring(0,idx2);
                
                String letter1 = str1.substring(idx1+1);
                String letter2 = str2.substring(idx2+1);
                
                if (str1.charAt(idx1+1) <= '9') {
                    if (str2.charAt(idx2+1) <= '9')
                        return 0;   // same digit logs
                    else
                        return 1;    // str2 is larger than str1
                }
                
                if (str2.charAt(idx2+1) <= '9')
                    return -1;      // str2 is less than str1
                
                // order by letter
                int preCompute = letter1.compareTo(letter2);
                // use id under same letter
                if (preCompute == 0) {
                    return id1.compareTo(id2);
                }
                
                return preCompute;
            }
        };
        Arrays.sort(logs, myComp);
        return logs;
    }
}