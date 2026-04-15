class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sqr = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num != ".":
                    b = (r // 3) * 3 + (c // 3)

                    if num in row[r] or num in col[c] or num in sqr[b]:
                        return False
                
                    row[r].add(num)
                    col[c].add(num)
                    sqr[b].add(num)
        return True
        