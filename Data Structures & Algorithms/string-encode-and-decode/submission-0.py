class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            length = len(i)
            prev = out
            out = str(str(length)+"#"+i)
            out = prev + out
        print("Encode : ",out)
        return out

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # find the #
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)

            i = j + 1 + length  # move pointer

        return res