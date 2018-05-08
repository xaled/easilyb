from easilyb.crawler import Crawler
from easilyb.urlselector.ratequeue import RateQueue
from easilyb.urlselector import UrlSelector
import unittest

# TODO: fix Crawler
count =0


def callback(url, response):
    global count
    count += 1


class CrawlerTest(unittest.TestCase):
    def testCount(self):
        crawler = Crawler(['http://www.hespress.com'], callback=callback, maxdepth=2, maxurls=20,
                          urlselector=UrlSelector())
        crawler.join()
        self.assertGreater(count,  0)

    def testCountRateQueue(self):
        crawler = Crawler(['http://www.hespress.com'], callback=callback, maxdepth=2, maxurls=20,
                          urlselector=RateQueue())
        crawler.join()
        self.assertGreater(count,  0)

if __name__ == "__main__":
    unittest.main()