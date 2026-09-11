class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater=0
        i=0
        j=len(height)-1


        while(i<j):
            mini=min(height[i] , height[j])
            water=mini*(j-i)
            maxwater=max(maxwater, water)
            if (height[i]<height[j]):
                i+=1
            else:
                j-=1
        return maxwater
        

        

       
        # maxsum=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)): # here time limit exceeded
        #         mini=min(height[i],height[j])
        #         maxi=mini*(j-i)
        #         maxsum=max(maxsum,maxi)
        # return maxsum

        

            

                
        