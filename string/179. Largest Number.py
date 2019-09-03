# 179. Largest Number
"""
python: cmp compare function
def compare(x,y):
    return x-y  increasing
    return y-x  decreasing

python: lstrip('A): from left skip 'A'
"""

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a,b):
            return int(b+a) - int(a+b)
        nums = sorted([str(x) for x in nums], cmp=compare)
        # pay atterntion to skip leading 0
        ans = ''.join(nums).lstrip('0')
        return ans or '0'