class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            
        self.store[key].append([value, timestamp])

    # Use Binary search heavily in both of this. 
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        # USE THAT BINARY SEARCH
        val_arr = self.store[key]
        result = ""

        l = 0
        r = len(val_arr) - 1

        while l <= r:
            m = l + (r - l) // 2

            value = val_arr[m][0]
            store_timestamp = val_arr[m][1]

            # Gets the timestamp of the dead center item in the list value for the given key.
            if store_timestamp <= timestamp:
                result = value
                l = m + 1
            else:
                r = m - 1
                
        return result

        
