# class Solution:
#     def countCommas(self, n: int) -> int:
#         s=str(n)
#         if len(s)<4:
#             return 0
#         elif len(s)==4:
#             return n-1000 + 1
#         else:
#             return n-10000 + 1


class Solution:
    def countCommas(self, n: int) -> int:
        s = len(str(n))
        if s < 4:
            return 0
        ans = 0
        base = 1000
        while base <= n:
            ans += n - base + 1
            base = base * 1000
        return ans
