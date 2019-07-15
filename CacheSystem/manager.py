from LRU_cache import *
from helpers import print_cache, print_options, url_verifier, get_url_index, read_yaml

import random

one = LRUCacheURL(1, 'https://www.google.com/')
two = LRUCacheURL(2, 'www.facebook.com')
three = LRUCacheURL(3, 'www.twitter.com')
# Setup
cache = LRUCache(length=3, alpha=5)
cache.insert_url(one)
cache.insert_url(two)
cache.insert_url(three)


if __name__ == '__main__':

    i = random.randint(0, 128)
    j = random.randint(128, 512)
    key = random.randint(i, j)

    while True:
        print_options()
        i = input('Selection:')
        if i == 1:
            print_cache(cache)
        if i == 2:
            print(read_yaml('capacity'))
        if i == 3:
            pass
        if i == 4:
            # Option to input and insert in cached mem.
            input_url = "'" + str(raw_input('Insert the url:')) + "'"
            # insert in cache
            it = LRUCacheURL(key, input_url)
            cache.insert_url(it)
            key = random.randint(i, j)
            i = random.randint((i+j) // 2, ((i+j) * 3) // 2)
        if i == 5:
            index = input('Insert the index of the url:')
            verify_url = get_url_index(cache, index)
            if url_verifier(verify_url) is not None:
                print('The URL is correct.')
            else:
                print('The URL is incorrect.')
        if i == 7:
            print("Ai de plm poate merge.")
        if i == 0:
            break
