class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=moves.count("U")
        b=moves.count("L")
        c=moves.count("R")
        d=moves.count("D")
        if a==d and b==c:
            return True
        else :
            return False 
        
        