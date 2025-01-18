from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.memory = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.memory[key]
        idx = self._search(values, timestamp)
        values.insert(idx + 1, [timestamp, value])
        self.memory[key] = values

    def get(self, key: str, timestamp: int) -> str:
        values = self.memory[key]
        if len(values) == 0:
            return ""
        idx = self._search(values, timestamp)
        if idx >= 0 and idx < len(values) and values[idx][0] <= timestamp:
            return values[idx][1]
        if idx > 0:
            return values[idx - 1][1]
        return ""
        

    def _search(self, values: List[int], timestamp: int) -> int:
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) >> 1
            if values[mid][0] == timestamp:
                return mid
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)