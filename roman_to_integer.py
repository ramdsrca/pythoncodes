class Solution:
    # def romanToInt(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     roman = {'I': 1, 'V': 5, 'X': 10,
    #              'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     result = 0
    #     last = s[-1]
    #     for t in reversed(s):
    #         if t == 'C' and last in ['D', 'M']:
    #             result -= roman[t]
    #         elif t == 'X' and last in ['L', 'C']:
    #             result -= roman[t]
    #         elif t == 'I' and last in ['V', 'X']:
    #             result -= roman[t]
    #         else:
    #             result += roman[t]
    #         last = t
    #     return result

    def romanToInt(self, s) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, total = 0, 0
        
        for c in s.upper():
            curr = roman[c]
            total += curr
            print("curr: ", curr , " total: ", total, " prev: ", prev)
            # need to subtract
            if curr > prev:
                total -= 2 * prev
                print("inside curr>prev: ", curr , " total: ", total, " prev: ", prev)
            prev = curr
        return total

run = Solution()
print("running romantoInt VIII " , run.romanToInt("VIII")) # 8
print("running romantoInt LXVII " , run.romanToInt("LXvII")) # 367