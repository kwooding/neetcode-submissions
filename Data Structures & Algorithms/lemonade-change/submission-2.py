class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {}
        for p in bills:
            if p not in change:
                change[p] = 0
            change[p] += 1
            if p == 5:
                continue
            elif p == 10:
                if change.get(5, 0) < 1:
                    return False
                change[5] -= 1
            elif p == 20:
                if change.get(10, 0) < 1:
                    if change.get(5, 0) < 3:
                        return False
                    change[5] -= 3
                else: 
                    change[10] -= 1
                    if change.get(5, 0) < 1:
                        return False
                    change[5] -= 1
 
        return True
        
            


