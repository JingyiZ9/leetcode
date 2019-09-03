# 291. Word Pattern II

#########
# 回溯法：backtracking
# 走不通就返回，利用递归实现
# 建立pattern和word之间的映射关系： 两个hashtab
# 用变量p记录当前递归到的pattern位置，用r记录当前单词串str的位置

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, strs):
        # map1 record pattern and map2 record strs
        map1, map2 = {},{}
        return self.match(pattern,strs,0,0,map1,map2)
        
    def match(self,pattern,strs,i,j,map1,map2):
        is_match = False
        if i == len(pattern) and j == len(strs):
            is_match = True
        if i < len(pattern) and j < len(strs):
            # i is the current position for pattern
            # j is the current position for strs
            p = pattern[i]
            if p in map1:
                # p should be matched to w in strs
                w = map1[p]
                if w == strs[j:j+len(w)]:
                    # recursion
                    is_match = self.match(pattern,strs,i+1,j+len(w),map1,map2)
            else:   # p is not in map1
                # try to build the new reflection between p and w
                for k in range(j,len(strs)):
                    w = strs[j:k+1]
                    # w should be not used in map2
                    if w not in map2:
                        map1[p] = w
                        map2[w] = p
                        # recursion
                        is_match = self.match(pattern,strs,i+1,k+1,map1,map2)
                        # if is_match == False, pop built relationship
                        map1.pop(p)
                        map2.pop(w)
                        if is_match == True:
                            break
        return is_match