class Solution:
    def largestOddNumber(self, num: str) -> str:
        i=len(num)-1
        ans=""
        while i>=0:
            if int(num[i])%2!=0:
                ans=num[0:i+1]
                return ans 
            i-=1
        return ans