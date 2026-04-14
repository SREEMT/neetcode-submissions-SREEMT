class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_string = ""
        for s in strs:
            l = len(s)
            enc_string = enc_string + f"{l}" + "#" + s
        return enc_string

    def decode(self, s: str) -> List[str]:
        dec_strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            l = int(s[i:j])
            dec_strs.append(s[j + 1 : j + 1 + l])
            i = j + 1 + l
        return dec_strs
