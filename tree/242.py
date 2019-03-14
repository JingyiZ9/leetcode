---
layout: post
title:  "242 sort two strings"
permalink: /242. valid anagram/
---

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        
        if s == t:
            return True
        else:
            return False