# 충돌(collision)
# 1. Chaning 기법: 충돌이 발생했을 때, 그 값들을 링크드 리스트로 관리

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

linked_tuple = LinkedTuple()
linked_tuple.add("333", 7)
linked_tuple.add("77", 6)

class LinkedDict:
    def __init__(self):
        self.items = []

        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value) # index번째의 LinkedTuple[(key, value)]
                                          # 한번 더 호출되면? -> index번째의 LinkedTuple[(key, value), (key2, value2)]

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key) # LinkedTuple [(key, value), (key2, value2)]


my_dict = LinkedDict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!