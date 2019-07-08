from LRU_cache import *

one = LRUCacheURL(1, 'www.google.com')
two = LRUCacheURL(2, 'www.facebook.com')
three = LRUCacheURL(3, 'www.twitter.com')

# Setup
cache = LRUCache(length=3, alpha=5)
cache.insert_url(one)
cache.insert_url(two)
cache.insert_url(three)


def print_cache(curr_cache):
    """ Function to print contents of cached mem."""
    for index, url in enumerate(curr_cache.url_list):
        print('index: {} '
              'key: {} '
              'url: {} '
              'timestamp: {} '.format(index,
                                      url.key,
                                      url.url,
                                      url.timestamp))


if __name__ == '__main__':
    print_cache(cache)
