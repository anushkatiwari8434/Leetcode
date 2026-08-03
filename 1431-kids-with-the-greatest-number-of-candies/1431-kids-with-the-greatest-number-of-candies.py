class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        maxCandies=max(candies)
        for i in candies:
          if(i+extraCandies>=maxCandies):
            ans.append(True)
          else:
             ans.append(False)
        return ans       
        