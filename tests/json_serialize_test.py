import easilyb.json_serialize as jsons
import unittest


class TestSerializable(jsons.JsonSerializable):
    def __init__(self, a, b):
        self.a = a
        self._temp = b


class TestSerializable2(jsons.get_serializable_class(meta_prefix="__")):
    def __init__(self, a, b):
        self.a = a
        self._temp = b


class JsonSerializeTest(unittest.TestCase):
    def test_serilizable_class(self):
        test = TestSerializable('testa', 'testb')
        json_dump = jsons.dumps({'test':test})
        print(json_dump)
        self.assertTrue(True)
        json_load = jsons.loads(json_dump)
        self.assertIsInstance(json_load['test'], TestSerializable)
        self.assertEqual(test.a, json_load['test'].a)
        self.assertNotIn('_temp', json_load['test'].__dict__)

    def test_binary_string(self): #TODO: python2 support
        test = b'aaaa\x00\xf0\xab\xffddddmfdlksdmflkd'
        test_dump = jsons.dumps({'test':test})
        print(test_dump)
        test_load = jsons.loads(test_dump)['test']
        self.assertIsInstance(test_load, bytes)
        self.assertEqual(test_load, test)

    def test_set_n_tuple(self):
        t = (1,2,3)
        s = set(t)
        test = {'s':s, 't':t}
        test_dump = jsons.dumps(test)
        print(test_dump)
        test_load = jsons.loads(test_dump)
        # self.assertIsInstance(test_load['t'], tuple)
        self.assertIsInstance(test_load['s'], set)

    def test_serilizable_class_n(self):
        test = TestSerializable2('testa', 'testb')
        json_dump = jsons.dumps({'test':test}, meta_prefix="__")
        print(json_dump)
        self.assertTrue(True)
        json_load = jsons.loads(json_dump, meta_prefix="__")
        self.assertIsInstance(json_load['test'], TestSerializable2)
        self.assertEqual(test.a, json_load['test'].a)
        self.assertNotIn('_temp', json_load['test'].__dict__)



if __name__ == "__main__":
    unittest.main()