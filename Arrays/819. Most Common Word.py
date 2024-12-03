# Most Common Word

import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        p = re.split(r'\W+', paragraph.lower())

        q = [w for w in p if w not in banned and w != '']

        return max(q, key = q.count) 
