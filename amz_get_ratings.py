import bottlenose
from bs4 import BeautifulSoup
import secret as sk

#api = amazonproduct.API(cfg=config)

amazon = bottlenose.Amazon(sk.AMZ_KEY, sk.AMZ_SECRET, sk.AMZ_TAG, Parser=BeautifulSoup)

results = amazon.ItemSearch(Keywords=('Star Trek', 'Next Generation', 'series'), SearchIndex="All")

for i, response in enumerate(results):
    print "{0}. '{1}'".format(i, response.title)
    print len(results)
