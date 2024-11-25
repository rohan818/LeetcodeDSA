# Baseball Game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rlist = []
        for i in operations:
            if i == '+':
                rlist.append(rlist[-1] + rlist[-2])
            elif i == 'C':
                rlist.pop()
            elif i == 'D':
                rlist.append(2 * rlist[-1])
            else:
                rlist.append(int(i))
        
        return sum(rlist)
