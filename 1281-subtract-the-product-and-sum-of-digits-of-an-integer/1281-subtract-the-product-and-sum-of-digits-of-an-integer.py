class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        original=n
        sum=0
        prod=1
        result=0
        while n>0:
            digit=n%10
            sum=sum+digit
            prod=prod*digit
            n//=10
        result=prod-sum
        return result    
            

        