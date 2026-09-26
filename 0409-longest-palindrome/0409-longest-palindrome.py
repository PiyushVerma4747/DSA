class Solution:
    def longestPalindrome(self, s: str) -> int:
        n=len(s)
        dic={}
        for i in s:
            if i in dic:dic[i]+=1
            else:dic[i]=1
        ans=0
        for i in dic:
            if dic[i]%2==0:ans+=dic[i]
            else:ans+=dic[i] - 1
        if  ans<n:
            return ans + 1
        else:
            return ans
        