import collections
import unittest


def log_decorate(func):
    def wrapper(*args):
        func_name = func.__name__
        if func_name == 'get':
            r = func(*args)
            print("{0} key: {1} value: {2}".format(func_name, args[1], r))
            return r
        if func_name == 'put':
            func(*args)
            print("{0} key: {1} value: {2}".format(func_name, args[1], args[2]))
    return wrapper


class LRUCache(object):

    def __init__(self, max_size=100):
        self.dic = collections.OrderedDict()
        self.capacity = max_size

    @log_decorate
    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v
        return v

    @log_decorate
    def put(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1  
            else:
                self.dic.popitem(last=False) 
        self.dic[key] = value


class TestFindAnagrams(unittest.TestCase):
    def test_get_value_from_empty(self):
        lru = LRUCache()
        v = lru.get(1)
        self.assertEqual(v, -1)

    def test_get_value_key_not_exist(self):
        lru = LRUCache()
        lru.put(1,'a')
        v = lru.get(2)
        self.assertEqual(v, -1)

    def test_get_value_key_exist(self):
        lru = LRUCache(3)
        lru.put(1,'a')
        v = lru.get(1)
        self.assertEqual(v, 'a')

    def test_remove_last(self):
        lru = LRUCache(3)
        lru.put(1,'a')
        lru.put(2,'b')
        lru.put(3,'c')
        lru.put(4,'d')
        self.assertEqual(lru.dic, {2:'b',3:'c',4:'d'})

    def test_get_reorder(self):
        lru = LRUCache(3)
        lru.put(1,'a')
        lru.put(2,'b')
        lru.put(3,'c')
        v = lru.get(1)
        self.assertEqual(lru.dic, {2:'b',3:'c',1:'a'})

    def test_default_max_size(self):
        lru = LRUCache()
        self.assertEqual(lru.capacity, 100)


if __name__ == "__main__":
    unittest.main()