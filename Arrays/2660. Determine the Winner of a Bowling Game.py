# Determine the Winner of a Bowling Game
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        count = 0
        count1 = 0
        s1,s2 = 0,0
        for i,j in zip(player1,player2):

            if count==0:
                s1+=i
            else:
                s1+= 2*i
            if count1==0:
                s2+=j
            else:
                s2+= 2*j
            if count>0:
                count-=1
            if count1>0:
                count1-=1
            if i==10:
                count=2
            if j==10:
                count1=2
            
        if s1>s2:
            return 1
        elif s2>s1:
            return 2
        return 0
