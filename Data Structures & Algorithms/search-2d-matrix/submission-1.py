class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        x = len(matrix) - 1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                x = i - 1
                break

            elif matrix[i][0] == target:
                return True

        l, r = 0, len(matrix[x]) - 1
        if matrix[x][l] == target or matrix[x][r] == target:
            return True
        while l < r:
            m = (l+r)//2
            print("m: ",m)
            print("l, r: ", l, r)
            if target == matrix[x][m]:
                return True
            elif target < matrix[x][m]:
                r = m
            else:
                l = m + 1


        return False