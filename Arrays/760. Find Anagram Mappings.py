# Find Anagram Mappings
def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []
        
        for i in nums1:
            mapping.append(nums2.index(i))

        return mapping
