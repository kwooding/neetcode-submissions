class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        print(max(arr[:]))
        for i in range(len(arr)):
            if i == (len(arr) - 1):
                arr[i] = -1
            else:
                r = max(arr[i+1:])
                arr[i] = r
        
        return arr