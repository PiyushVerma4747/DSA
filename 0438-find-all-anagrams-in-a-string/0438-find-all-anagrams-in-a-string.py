# class Solution: #7394 ms
#     def findAnagrams(self, s: str, p: str) -> list[int]:
#         n=len(p)
#         p=sorted(p)
#         l=[]
#         i=0
#         while n+i <= len(s) :
#             if p==sorted(s[i:i+n]):l.append(i)
#             i+=1
#         return l

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        count_p = [0] * 26 # store freq of char in p
        count_s = [0] * 26 # store freq of char in curr window 
        for ch in p:
            count_p[ord(ch) - ord('a')] += 1
        n = len(p)
        ans = []
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1

            if i >= n: # if window size increses to ham purane letter ki freq kam karenge
                count_s[ord(s[i-n]) - ord('a')] -= 1

            if count_s == count_p: # agar dono array same hai matlab freq samer hai yhen curr window is anagrm
                ans.append(i - n + 1)

        return ans
        