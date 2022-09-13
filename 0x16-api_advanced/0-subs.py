#!/usr/bin/python3
'''prints actual suscribers for given subreddit'''


def number_of_subscribers(subreddit):
    '''prints actual suscribers for given subreddit'''
    import requests
    from sys import argv

    headers = {'User-Agent': 'Mozilla/5.0\
              (Windows NT 6.1; Win64; x64; rv:47.0)\
              Gecko/20100101 Firefox/47.0'}

    url = 'https://api.reddit.com/r/{}/about'.format(argv[1])
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.json().get('data'):
        return (r.json().get('data').get('subscribers'))
    return (0)
