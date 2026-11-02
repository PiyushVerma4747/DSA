class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        n1=str(x)
        n2=n1[::-1]
        print(n2)
        if(n1==n2):
            return True
        else:
            return False
        