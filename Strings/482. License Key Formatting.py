#
def licenseKeyFormatting(self, s: str, k: int) -> str:
    s = s.replace('-', '').upper()

    n = len(s)
    f_group_len = n % k or k
    res = [s[:f_group_len]]

    for i in range(f_group_len, n, k):
        res.append(s[i:i+k])
    return '-'.join(res)
