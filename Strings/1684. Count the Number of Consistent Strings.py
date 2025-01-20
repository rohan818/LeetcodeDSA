# Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_count = 0
        for word in words:
            if all(char in allowed for char in word):
                consistent_count += 1
        
        return consistent_count
