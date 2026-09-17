class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=max(nums)
        dic={}
        if n + 1 !=len(nums):
            return False
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]>=2 and i!=n:
                return False
        req=n*(n+1)//2 + n
        summ=sum(nums)
        print(req  , summ)
        if summ == req:
            return True
        else:
            return False
        