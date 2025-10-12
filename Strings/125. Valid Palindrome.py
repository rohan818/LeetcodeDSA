#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]+', '', s.lower())
        return s == s[::-1]

    # s = ''.join(c.lower() for c in s if c.isalnum())
    # return s == s[::-1]
