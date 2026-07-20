class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        print(counts)
        max_odd, min_even = 0, float('inf')
        for c in counts.values():
            if c % 2 == 0 and c < min_even:
                min_even = c
            elif c % 2 != 0 and c > max_odd:
                max_odd = c

            
        return max_odd - min_even