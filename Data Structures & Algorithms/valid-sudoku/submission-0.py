class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # ROWS
        for row in board:
            prev = set()
            for column in row:
                if (column in prev):
                    return False
                
                if (column != "."):
                    prev.add(column)
        
        print("Pass")
            
        for i in range(len(board)):
            prev = set()
            for j in range(len(board)):
                num = board[j][i]

                print(num)
                if (num in prev):
                    print(prev)
                    return False

                if (num != "."):
                    prev.add(num)

        print("Pass")

        for i in range(3):
            for j in range(3):
                prev = set()
                for k in range(i*3, i*3+3):
                    for l in range(j*3, j*3+3):
                        num = board[k][l]
                        
                        print(num)

                        if (num != "." and num in prev):
                            return False

                        if (num != "."):
                            prev.add(num)   

        return True


            


        