class Solution:
    def lowerBound(self,nums,target):
        n=len(nums)
        l=0
        r=n-1
        ans=n
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>= target: 
                ans=mid
                r=mid-1
            else:
                l=mid+1  
        return ans 
    def upperBound(self,nums,target):
        n=len(nums)
        l=0
        r=n-1
        ans=n
        while l<=r:
            mid=(l+r)//2
            if nums[mid]> target: 
                ans=mid
                r=mid-1
            else:
                l=mid+1  
        return ans         
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.lowerBound(nums, target)
        last = self.upperBound(nums, target) - 1

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        return [first, last]