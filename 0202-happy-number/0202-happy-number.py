# class Solution:
#     def isHappy(self, n: int) -> bool:
#         # if n//10==0 and n!=1:
#         #     return False
#         temp=n
#         i=0
#         while temp!=1 and i<31:
#             sum_sq=0
#             while temp > 0 :
#                 rem=temp%10
#                 sum_sq+=rem*rem
#                 temp=temp//10
#             temp=sum_sq
#             i+=1
#         if temp==1:
#             return True
#         else:
#             return False

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            sum_sq = 0
            while n > 0:
                rem = n % 10
                sum_sq += rem * rem
                n //= 10
            n = sum_sq
        return n == 1




        