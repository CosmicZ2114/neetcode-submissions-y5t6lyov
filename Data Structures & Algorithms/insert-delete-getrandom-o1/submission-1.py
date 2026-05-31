import random
class RandomizedSet:
    def __init__(self):
        self.val_dic={}
        self.li=[]

    def insert(self, val: int) -> bool:
        if val in self.val_dic:
            return False
        self.val_dic[val]=len(self.li)
        self.li.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val in self.val_dic:
            ids=self.val_dic[val]
            lst=self.li[-1]
            self.li[ids] = lst
            self.val_dic[lst] = ids
            self.li.pop()
            del self.val_dic[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.li)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()