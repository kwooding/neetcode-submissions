class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = defaultdict(str)
        for i in range(len(order)):
            alphabet[order[i]] = i

        #print(alphabet)
        res_list = []
        for word in words:
            res = []
            for ch in word:
                res.append(alphabet[ch])
            res_list.append(res)

        return res_list == sorted(res_list)