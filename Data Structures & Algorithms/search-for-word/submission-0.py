class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #get dimensions
        ROWS,COLS= len(board),len(board[0])
        #follow our path with no duplicates
        path = set()

        #r:row,c:column,i:current char
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r<0 or c<0 or 
                r>= ROWS or c>=COLS or 
                word[i] != board[r][c] or 
                (r,c) in path):
                return False

            #not out of bounds or repeating so we add
            path.add((r,c))


            #check in each direciton
            res = (dfs(r+1,c,i+1))or (dfs(r-1,c,i+1)) or (dfs(r,c+1,i+1)) or (dfs(r,c-1,i+1))

            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False


    
        
        





