class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right + 1):
            num = i
            valid = True

            while num > 0:
                digit = num % 10

                if digit == 0 or i % digit != 0:
                    valid = False
                    break

                num //= 10

            if valid:
                ans.append(i)

        return ans