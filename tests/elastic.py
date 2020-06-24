from easilyb.databases.elasticsearch import ElasticDB
from easilyb.string_ops import random_string
import time

import unittest

elastic_db = ElasticDB(docker_server=True, stop_at_exit=False)


def generate_docs():
    docs = list()
    for i in range(20):
        docs.append({'i': i, 'text': random_string()})
    return docs


class ElasticTest(unittest.TestCase):
    def test_dict_methods(self):
        key = random_string()
        txt = random_string()
        elastic_db[key] = {'text': txt}
        self.assertIn(key, elastic_db)
        self.assertEqual(elastic_db[key]['text'], txt)
        del elastic_db[key]
        self.assertIsNone(elastic_db[key])

    def test_bulk_index_delete(self):
        test_id = random_string()
        objects = {random_string(): {'text': random_string(), 'test_id': test_id, 'i': i} for i in range(50)}
        count0 = len(elastic_db)
        resp = elastic_db.bulk_index(objects)
        time.sleep(1)
        self.assertEqual(len(elastic_db), count0 + len(objects))
        deleted = elastic_db.delete_by_query("test_id:" + test_id)
        self.assertEqual(deleted, len(objects))
        elastic_db.bulk_index(objects)
        elastic_db.bulk_delete(list(objects.keys()))
        time.sleep(1)
        self.assertEqual(len(elastic_db), count0)

    def test_iter_search(self):
        test_id = random_string()
        objects = {random_string(): {'text': random_string(), 'test_id': test_id, 'i': i} for i in range(50)}
        elastic_db.bulk_index(objects)
        time.sleep(1)
        count0 = len(elastic_db)
        c = 0
        for doc in elastic_db.search_after(size=5, sort='_doc'):
            c += 1
        self.assertEqual(c, count0)
        c = 0
        for doc in elastic_db:
            c += 1
        self.assertEqual(c, count0)


if __name__ == "__main__":
    unittest.main()