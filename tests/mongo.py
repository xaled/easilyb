from easilyb.databases.mongo import MongoDB
from easilyb.string_ops import random_string

import unittest

mongo_db = MongoDB(docker_server=True, stop_at_exit=False)


def generate_docs():
    docs = list()
    for i in range(20):
        docs.append({'i': i, 'text': random_string()})
    return docs


class MongoTest(unittest.TestCase):
    def test_dict_methods(self):
        key = random_string()
        txt = random_string()
        mongo_db[key] = {'text': txt}
        self.assertIn(key, mongo_db)
        self.assertEqual(mongo_db[key]['text'], txt)
        del mongo_db[key]
        self.assertIsNone(mongo_db[key])

    def test_bulk_set_delete(self):
        test_id = random_string()
        objects = {random_string(): {'text': random_string(), 'test_id': test_id, 'i': i} for i in range(50)}
        count0 = len(mongo_db)
        resp = mongo_db.bulk_set(objects)
        self.assertEqual(len(mongo_db), count0 + len(objects))
        mongo_db.bulk_delete(list(objects.keys()))
        self.assertEqual(len(mongo_db), count0)

    def test_iter_search(self):
        test_id = random_string()
        objects = {random_string(): {'text': random_string(), 'test_id': test_id, 'i': i} for i in range(50)}
        mongo_db.bulk_set(objects)
        count0 = len(mongo_db)
        c = 0
        for doc in mongo_db:
            c += 1
        self.assertEqual(c, count0)


if __name__ == "__main__":
    unittest.main()
