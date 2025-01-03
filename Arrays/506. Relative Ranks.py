# Relative Ranks
from collections import defaultdict
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        score1 = score.copy()

        score_index_d = defaultdict(int)
        for i in range(n):
            score_index_d[score1[i]] = i
        
        score1.sort(reverse=True)

        rank = [" "]*n
        for i in range(n):
            if i == 0:
                rank[score_index_d[score1[i]]] = "Gold Medal"
            elif i == 1:
                rank[score_index_d[score1[i]]] = "Silver Medal"
            elif i == 2:
                rank[score_index_d[score1[i]]] = "Bronze Medal"
            else:
                rank[score_index_d[score1[i]]] = str(i + 1)
        
        return rank
