class Link:
    def __init__(self, val) -> None:
        self.value = val


class LRUCache:
    
    def __init__(self, capacity: int):
        self.lru_cache = dict()
        self.capacity = capacity
        self.next_rank = 0

        
        
        

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1
        # access item and return it's value
        self.lru_cache[key][1] = self.next_rank
        self.next_rank += 1
        return self.lru_cache[key][0]
    
    def put(self, key: int, value: int) -> None:
        if len(self.lru_cache) == self.capacity:
            if key not in self.lru_cache:
                lru = min(self.lru_cache.keys(), key=lambda x: self.lru_cache[x][1])
                self.lru_cache.pop(lru)                

        self.lru_cache[key] = [value, self.next_rank]
        self.next_rank += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
x = {2:1,1:1}
