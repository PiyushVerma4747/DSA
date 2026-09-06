# class Solution: #
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums)==1:
#             return True
#         i=0
#         while i <= len(nums):
#             if nums[i]==0:
#                 return False
#             if i+nums[i]>len(nums) - 1:
#                 return True 
#             i+=nums[i] 
#         return False

class Solution: # greedy algorithm 
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach , i + nums[i])
        return True
        
        