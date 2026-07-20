class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        res = 0
        

        while True:
            check = ""

            for c in "balloon":
                if counts.get(c,0) >= 1:
                    check += c
                    counts[c] -= 1

                else:
                    return res

            if check == "balloon":
                res += 1

        
