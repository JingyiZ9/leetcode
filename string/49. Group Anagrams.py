# 49. Group Anagrams

# hashtab: time limited exceeded
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for i in range(len(strs)):
            dict_s = collections.Counter(strs[i])
            flag = 0
            for j in range(len(res)):
                dict_res = collections.Counter(res[j][0])
                if dict_s == dict_res:
                    res[j] += [strs[i]]
                    flag = 1
                    break
            if flag == 0:
                res += [[strs[i]]]
        return res

# hashtab, key is sorted element in strs
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for ele in strs:
            tmp = ele
            key = ''.join(sorted(tmp))
            if key in d:
                d[key] += [ele]
            else:
                d[key] = [ele]
        for val in d.values():
            res += [val]
        return res