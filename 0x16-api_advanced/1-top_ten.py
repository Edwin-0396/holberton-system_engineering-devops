#!/usr/bin/python3
'''prints actual top 10 hot post for given subreddit'''


def top_ten(subreddit):
    '''prints top 10 hot for given subreddit'''
    import requests
    from sys import argv

    headers = {'User-Agent': 'Mozilla/5.0\
              (Windows NT 6.1; Win64; x64; rv:47.0)\
              Gecko/20100101 Firefox/47.0'}

    url = 'https://api.reddit.com/r/{}/hot'.format(argv[1])
    r = requests.get(url, headers=headers, allow_redirects=False)
    i = 0
    if r.json().get('data'):
        for key in r.json().get('data').get('children'):
            i += 1
            print(key.get('data').get('title'))
            if i == 10:
                break
    else:
        print(None)
