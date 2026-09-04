# class Solution:
#     def firstStableIndex(self, nums: list[int], k: int) -> int:
#         n=len(nums)
#         maxx=[0]*n
#         minn=[0]*n
#         curr_minn=nums[-1]
#         curr_maxx=nums[0]
#         for i in range(len(nums)):
#             j=n-1-i
#             curr_maxx=max(curr_maxx,nums[i])
#             curr_minn=min(curr_minn,nums[j])
#             minn[j]=curr_minn
#             maxx[i]=curr_maxx
#         for i in range(len(nums)):
#             if maxx[i]-minn[i] <=k:
#                 return i
#         return -1

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix minimum
        right = [0] * n
        right[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])

        # prefix maximum + check
        left = nums[0]

        for i in range(n):
            left = max(left, nums[i])

            if left - right[i] <= k:
                return i

        return -1
        