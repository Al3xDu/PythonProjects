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


def print_options():
    print('1.Print memory cached.')
    print('2.Print something idk.')
    print('3.Exit.')
