class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for i in strs:
            s1 = "".join(sorted(i))
            if s1 not in ans:
                ans[s1] = []
            ans[s1].append(i)

        return list(ans.values())
        