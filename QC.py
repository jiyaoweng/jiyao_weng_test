# python 3.6

Capacity = 4
testpages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.indexes = {}
        self.cache = set()

    def nextPage(self, currentPage):
        if len(self.cache) < self.capacity:
            if not currentPage in self.cache:
                self.cache.add(currentPage)
            self.indexes[currentPage] = self.count
        else:
            if not currentPage in self.cache:
                lru = 1000000
                val = -1000000
                for ss in self.cache:
                    if self.indexes[ss] < lru:
                        lru = self.indexes[ss]
                        val = ss

                self.cache.remove(val)
                self.cache.add(currentPage)
            self.indexes[currentPage] = self.count
        self.count += 1

#        print("indexes", self.indexes)
        return self.cache
	
    def getCache(self):
        return self.cache

# testing
lru = LRU(Capacity)

for page in testpages:
    cache = lru.nextPage(page)
    print("cache:", cache)
