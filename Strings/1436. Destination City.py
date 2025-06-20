#
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        has_out = set()
        for i in range(len(paths)):
            has_out.add(paths[i][0])
        
        for i in range(len(paths)):
            item = paths[i][1]
            if item not in has_out:
                return item
        
        return ""
