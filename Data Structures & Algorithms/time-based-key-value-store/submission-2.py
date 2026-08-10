class TimeMap:

    def __init__(self):
        self.data = {} # store as name : [tstmp1,tstmp2,tstmp3]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        arr = self.data[key]
        lo, hi = 0, len(arr) - 1
        result = ""

        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= timestamp:
                # this timestamp is a valid candidate — record it,
                # but keep looking to the right for something closer to timestamp
                result = arr[mid][1]
                lo = mid + 1
            else:
                # arr[mid][0] is too big, look to the left
                hi = mid - 1

        return result
