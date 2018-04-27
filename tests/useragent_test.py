import xaled_utils.net
import unittest


class UserAgentTest(unittest.TestCase):
    def testUniq(self):
        ua_set = set()
        for i in range(100):
            ua = xaled_utils.net.get_useragent()
            print(ua)
            ua_set.add(ua)
        self.assertGreater(len(ua_set), 70)
