from LRU_cache import *
from helpers import print_cache, print_options

import regex as re

one = LRUCacheURL(1, 'www.google.com')
two = LRUCacheURL(2, 'www.facebook.com')
three = LRUCacheURL(3, 'www.twitter.com')

# Setup
cache = LRUCache(length=3, alpha=5)
cache.insert_url(one)
cache.insert_url(two)
cache.insert_url(three)

regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


if __name__ == '__main__':
    print(re.match(regex, '///aaa.com') is not None)
    while True:
        print_options()
        i = input('Selection:')
        if i == 1:
            print_cache(cache)
        if i == 2:
            print("Ai de plm poate merge.")
        if i == 3:
            break
