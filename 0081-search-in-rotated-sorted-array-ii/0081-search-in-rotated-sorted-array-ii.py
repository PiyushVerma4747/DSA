class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        lo=0
        hi=n-1
        while lo <= hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return True
            if nums[lo]==nums[hi]==nums[mid]:
                lo+=1
                hi-=1
            elif nums[lo]<=nums[mid]: # left side is sorted 
                if nums[lo]<=target and target < nums[mid]:
                    hi=mid-1
                else:
                    lo=mid + 1
            else: # right agar sot hai
                if nums[mid]<target and target <= nums[hi]:
                    lo=mid + 1
                else:
                    hi=mid - 1
        return False