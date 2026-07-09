class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers = set(numbers)
        result = list()
        for n in numbers:
            rem = target -n
            if rem in numbers:
                result.append(numbers.index(n) + 1)
                result.append(numbers.index(rem)+1)
                return result

        return list()