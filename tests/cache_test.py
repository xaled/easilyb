from easilyb.cache import SimpleCache, NotFoundInCache
import time
import unittest


v = 0


def get_value(k=0):
    global v
    v += 1
    return k + v


class CacheTest(unittest.TestCase):
    def xtest_put_n_get(self):
        global v
        v = 0
        cache = SimpleCache()
        cache.put("a", 5, ttl=2)
        cache.put("a", 10, ttl=2, namespace="walop")
        self.assertEqual(cache.get("a"), 5)
        self.assertEqual(cache.get("a", namespace="walop"), 10)
        time.sleep(3)
        self.assertEqual(cache.get("a", action=get_value, ttl=2), 1)
        self.assertEqual(cache.get("a", action=get_value, ttl=2), 1)
        time.sleep(3)
        self.assertEqual(cache.get("a", action=get_value, action_kwargs={"k":2}, ttl=2), 4)
        self.assertEqual(cache.get("a", action=get_value, action_kwargs={"k":2}, ttl=2), 4)
        time.sleep(3)
        try:
            cache.get("a")
        except NotFoundInCache:
            self.assertTrue(True)

    def test_put_n_get2(self):
        global v
        v = 0
        cache = SimpleCache(ttl=2)
        cache.put("a", 5)
        cache.put("a", 10, namespace="walop")
        self.assertEqual(cache.get("a"), 5)
        self.assertEqual(cache.get("a", namespace="walop"), 10)
        time.sleep(3)
        self.assertEqual(cache.get("a", action=get_value), 1)
        self.assertEqual(cache.get("a", action=get_value), 1)
        time.sleep(3)
        self.assertEqual(cache.get("a", action=get_value, action_kwargs={"k":2}), 4)
        self.assertEqual(cache.get("a", action=get_value, action_kwargs={"k":2}), 4)
        time.sleep(3)
        try:
            cache.get("a")
        except NotFoundInCache:
            self.assertTrue(True)

    def test_namespace_cache(self):
        global v
        v = 0
        main_cache = SimpleCache()
        cache = main_cache.get_namespace_cache("walopa")
        cache.put("a", 5, ttl=2)
        self.assertEqual(cache.get("a"), 5)
        time.sleep(3)
        self.assertEqual(cache.get("a", action=get_value, ttl=2), 1)
        self.assertEqual(cache.get("a", action=get_value, ttl=2), 1)
        time.sleep(3)
        self.assertEqual(cache.get("a", action=get_value, action_kwargs={"k":2}, ttl=2), 4)
        self.assertEqual(cache.get("a", action=get_value, action_kwargs={"k":2}, ttl=2), 4)
        time.sleep(3)
        try:
            cache.get("a")
        except NotFoundInCache:
            self.assertTrue(True)

    def test_decorator(self):
        cache = SimpleCache()
        global v
        v = 0
        @cache.cached(ttl=4)
        def get_value_ex(k=0):
            global v
            v += 1
            return k + v
        self.assertEqual(get_value_ex(), 1)
        self.assertEqual(get_value_ex(k=2), 4)
        self.assertEqual(get_value_ex(), 1)
        self.assertEqual(get_value_ex(k=2), 4)
        time.sleep(5)
        self.assertEqual(get_value_ex(), 3)
        self.assertEqual(get_value_ex(k=2), 6)
        self.assertEqual(get_value_ex(), 3)
        self.assertEqual(get_value_ex(k=2), 6)

    def test_decorator2(self):
        cache = SimpleCache(ttl=4)
        global v
        v = 0
        @cache.cached
        def get_value_ex(k=0):
            global v
            v += 1
            return k + v
        self.assertEqual(get_value_ex(), 1)
        self.assertEqual(get_value_ex(k=2), 4)
        self.assertEqual(get_value_ex(), 1)
        self.assertEqual(get_value_ex(k=2), 4)
        time.sleep(5)
        self.assertEqual(get_value_ex(), 3)
        self.assertEqual(get_value_ex(k=2), 6)
        self.assertEqual(get_value_ex(), 3)
        self.assertEqual(get_value_ex(k=2), 6)


if __name__ == "__main__":
    unittest.main()