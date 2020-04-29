#!/usr/bin/env python3
''' Link Verification

Author: Demi Franklin
'''
import argparse
import requests
import bs4

url = inpput('Enter URL Please: ')
res = requests.get(url)
res.raise_for_status()

def verify_links(url):
    url = input('Enter URL Please: ')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    links = soup.select('a')
    # list of links that lead to 404
    fof = []

    for link in links:
        try:
            unmade_url = link['href']
            if unmade_url.startswith('https'):
                to_check = unmade_url

            elif unmade_url.startswith('//'):
                to_check = 'https:' + unmade_url

            elif unmade_url.startswith('#'):
                to_check = url + unmade_url

            result = requests.get(to_check)

            if result.status_code == 404:
                fof.append(to_check)

        except:
            pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL to verify links')

    args = parser.parse_args()

    verify_links(args.url)

if __name__=='__main__':
    main()
