# class Solution:
#     def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
#         if xCenter-x1<=radius or xCenter-x2<=radius or yCenter-y1<=radius or yCenter-y1<=radius  or (xCenter-x1 + xCenter-x2)==(x2-x1) or (yCenter-y2 + yCenter-y1)==abs(y2-y1) :
#             return True
#         else:
#             return False        

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:

        x = max(x1, min(xCenter, x2))
        y = max(y1, min(yCenter, y2))

        return (x - xCenter) ** 2 + (y - yCenter) ** 2 <= radius ** 2