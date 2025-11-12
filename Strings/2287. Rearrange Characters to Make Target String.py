#
def rearrangeCharacters(self, s: str, target: str) -> int:
    res = []
    for char in set(target):  # Iterate over unique characters
        t_count = target.count(char)
        s_count = s.count(char)
        if t_count <= s_count:
            res.append(s_count // t_count)
        else:
            return 0
    return min(res)
