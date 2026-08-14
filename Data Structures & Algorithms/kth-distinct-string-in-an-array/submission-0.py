class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        count = 0
        print(d)
        for key in d:
            if d[key] == 1:
                count += 1
                if count == k:
                    return key
        

        return ""