import regex as re
import yaml


# func to verify an url with regex
def url_verifier(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None


# func to print cache
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


# func to get an url based on index
def get_url_index(curr_cache, index):
    """Return the url by the index."""
    for i, url in enumerate(curr_cache.url_list):
        if i == index:
            return url.url


# func to get url based on key
def get_url_key(curr_cache, key):
    """Return the url by the index."""
    for k, url in enumerate(curr_cache.url_list):
        if k == key:
            return url.url


# func to print options for the menu
def print_options():
    print('1.Print memory cached.')
    print('2.Read the length of the cache from a .yaml file.')
    print('3.Read the length of the cache from a .init file.')
    print('4.Create and insert a new url in cache.')
    print('5.Verify if an URL is correct.')
    print('6.Print something idk.')
    print('7.Funny message.')
    print('0.Exit.')


# func to read from a yaml file
def read_yaml(str_name):
    with open(str_name + ".yaml", 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            return exc
