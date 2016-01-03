from amazonproduct import API
import time as t

api = API(locale='us')
results = api.item_search('TV', title='Star Trek: The Next Generation')
results


#http://www.amazon.com/
#The-Naked-Now/dp
#/B00C30K9VU/ref=sr_1_2?s=movies-tv&ie=UTF8&
#qid=1451841012
#&sr=1-2&keywords=star+trek+next+generation
