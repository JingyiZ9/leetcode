# 290. Word Pattern
"""
give pattern and string to judge if the ont to one reflection
"""

# two hashtab for pattern and strs
class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        strs = string.split(" ")
        if len(strs) != len(pattern): return False
        # two hashtab
        map1, map2 = {}, {}
        for i in range(len(pattern)):
            if pattern[i] in map1:
                # check the reflection bwteen pattern and strs
                # one pattern already in the map1 should reflect just one strs
                if map1[pattern[i]] != strs[i]:
                    return False
            else:
                # appear a new pattern and it should reflect one strs that does not appear in map before
                if strs[i] in map2:
                    return False
                # update the map1: pattern and map2: string
                map1[pattern[i]] = strs[i]
                map2[strs[i]] = True
        return True