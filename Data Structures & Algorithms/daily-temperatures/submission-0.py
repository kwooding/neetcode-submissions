class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            count = 0
            if i != (len(temperatures) - 1):
                for j in range(i+1,len(temperatures)):
                    if temperatures[j] > currTemp:
                        count = j - i
                        break
                    
            
            res.append(count)

        return res