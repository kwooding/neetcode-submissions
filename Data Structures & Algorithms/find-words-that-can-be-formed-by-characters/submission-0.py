class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        counts = Counter(chars)

        for w in words:
            curr = Counter(w)
            good = True
            for c in curr:
                if curr[c] > counts[c]:
                    good = False
                    break

            if good:
                count += len(w)

        return count