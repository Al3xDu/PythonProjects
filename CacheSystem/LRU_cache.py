from datetime import datetime


class LRUCacheURL():
    """Data structures of the items stored in cache mem."""
    def __init__(self, key, url):
        self.key = key
        self.url = url
        self.timestamp = datetime.now()


class LRUCache():
    """ In this class is implemented the LRU Caching alg."""
    def __init__(self, length): # , alpha=None):
        self.length = length
        # self.alpha = alpha
        self.hash = []
        self.url_list = []

    def insertURL(self, url):
        """ Insert new urls to the cache."""
        if url.key in self.hash:
            # Move url to the head of the url_list
            url_index = self.url_list.index(url)
            self.url_list[:] = self.url_list[:url_index] + self.url_list[url_index + 1]
            self.url_list.insert(0, url)
        else:
            # If the length exceeds the cache's upper bound remove the last item
            if len(self.url_list) > self.length:
                self.removeURL(self.url_list[-1])
            # If this is a new url append it to the front of the list!
            self.hash[url.key] = url
            self.url_list.insert(0,url)

    def removeURL(self, url):
        """ Removes invalid urls."""
        del self.hash[url.key]
        del self.url_list[self.url_list.index(url)]




