// alien dictionary

class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        int len = words.length;
        int len_dic = order.length();
        
        // add order to the dict
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (int i=0; i<len_dic; i++) {
            map.put(order.charAt(i), i);
        }
        
        for (int i=0; i<len-1; i++) {
            if (!judge(words[i], words[i+1], map)) {
               return false; 
            }
        }
        return true;
    }
    
    public boolean judge(String word1, String word2, HashMap<Character, Integer> map) {
        int len1 = word1.length();
        int len2 = word2.length();
        int i=0;
        for (; i<len1 && i<len2; i++) {
            if (map.get(word1.charAt(i)) > map.get(word2.charAt(i)))
                return false;
            else if (map.get(word1.charAt(i)) < map.get(word2.charAt(i)))
                return true;
        }
        // compare the length if word1 matches word2: apple and app
        if (i<len1)
            return false;
        
        return true;
    }
}