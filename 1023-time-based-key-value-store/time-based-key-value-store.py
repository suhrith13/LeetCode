first we initialise a dictionary to store key- value pairs. If the key does not exist in self.dic, initialize it with an empty list.Append the [value, timestamp] pair to the list associated with the key in self.dic.
now we retireive the key value pairs from self.dic with the key value, then we use binary search to search the latest  value which is less than or equal to the given timestamp vallue.
initialise l, r to 0 and index - 1 and calculate the mid index. Now we check If the timestamp at mid is less than or equal to the given timestamp, update res with the value at mid and adjust l to search the right half of the list.
Otherwise, adjust r to search the left half of the list. finally we return res

class TimeMap:

    def __init__(self):
        self.dic = {}

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dic.get(key, [])
        l, r = 0 , len(values) - 1
        while l <= r:
            mid = (l + r) >> 1
            if values[mid][1] <= timestamp:
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1

        return res
        


