#!/usr/bin/python3
'''Returns a list of all hotlist'''


def recurse(subreddit, hot_list=[], next=None):
    '''Returns a list of all hotlist'''
    import requests

    headers = {'User-Agent': 'Mozilla/5.0\
              (Windows NT 6.1; Win64; x64; rv:47.0)\
              Gecko/20100101 Firefox/47.0'}

    params = {'after': next}

    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    r = requests.get(url, headers=headers,
                     allow_redirects=False, params=params)
    i = 0
    if r.json().get('data'):
        for key in r.json().get('data').get('children'):
            hot_list.append(key.get('data').get('title'))
        after = r.json().get('data').get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
