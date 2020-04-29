#!/usr/bin/env python3
# Downloads every single XKCD comic
import requests
import os

import bs4

# Starting URL
url = 'https://xkcd.com'
# Store commics in ./xkcd
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    '''Download the page'''
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    '''Find URL of comic image'''
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find commic image. Sorry, Charlie.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        '''Download image'''
        print('Downloading image %s...' % (comicUrl))

        res = requests.get(comicUrl)
        res.raise_for_status()

        '''Save image to ./xkcd.'''
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(1000000):
            imageFile.write(chunk)
        imageFile.close()

    '''Get Prev button's url'''
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Finished.')
