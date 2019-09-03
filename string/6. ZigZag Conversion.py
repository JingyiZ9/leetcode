# 6. ZigZag Conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) == 0:
            return s
        
        res = ""
        interval = 2*(numRows-1)
        for row in range(numRows):
            for j in range(row,len(s),interval):
                res += s[j]
                tmp = j + interval -2*row
                if row != 0 and row != numRows-1 and tmp < len(s):
                    res += s[tmp]
        return res