# Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)

        ptr_s = ptr_t = 0

        while ptr_s < s_len and ptr_t < t_len:
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t += 1

        return ptr_s == s_len
