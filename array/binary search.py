class solution:
    @staticmethod
    def binary_search(a,target):
        lower = 0
        upper = len(a)-1

        while upper > lower:
            mid = lower + (upper - lower) // 2
            val = a[mid]
            if val > target:
                upper = mid
            elif val < target:
                if lower == mid:
                    break
                lower = mid
                print(mid)
            else:
                return mid

        return -1

a = [2,3,5,6,7,8]
result = solution.binary_search(a, 9)
print(result)
