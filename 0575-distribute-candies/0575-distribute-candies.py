class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=set(candyType)
        l=len(s)
        can_eat=len(candyType)//2
        return min(can_eat,l)
        