class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        count = 0
        total = row * col
        cs = 0
        ce = col - 1
        rs = 0
        re = row - 1
        ans = []

        while count < total:
            for i in range(cs, ce + 1):
                ans.append(matrix[rs][i])
                count += 1
            rs += 1
            if count == total:
                break
            for i in range(rs, re + 1):
                ans.append(matrix[i][ce])
                count += 1
            ce -= 1
            if count == total:
                break
            for i in range(ce, cs - 1,-1):
                ans.append(matrix[re][i])
                count += 1
            re -= 1
            if count == total:
                break
            for i in range(re, rs - 1,-1):
                ans.append(matrix[i][cs])
                count += 1
            cs += 1
            if count == total:
                break

        return ans
