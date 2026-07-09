class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for w in words:
            for c in words:
                if w in c and w is not c:
                    res.add(w)

        return list(res)
