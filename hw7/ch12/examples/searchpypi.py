# Automatic execution
#!/usr/bin/env python3
'''searchpypi.py - Opens several serach results from pypi.org
'''
# Built-in Mods
import sys
import argparse
# 3rd party Mods
import webbrowser
import requests
import bs4
import pyperclip

# takes what is passed to the script and access it to become a name space
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('search', nargs='?')
    '''Corresponds to the number of links you want to open, with a default value of 5'''
    '''If n is provided it will show in the num-links name space, if not then 5'''
    # no dashes in python variable links
    parser.add_argument('-n', '--num-links', type=int, default=5)

    args = parser.parse_args()
    return args

# given search argumenys of the sring, it will build a url
def get_url(search):
    '''Given search string, return Url'''

    return f'https://pypi.org/search/?q={search}'

def get_project_url(path):
    '''Given a path, return a URL on pypi.org'''

    return f'https://pypi.org{path}'

def main():
    args = get_args()

    if args.search is None:
        '''Pull it from clipboard'''
        search = pyperclip.paste()
    else:
        search = args.search

    print('The given search terms:', search)

    url = get_url(search)

    print('The URL is:', url)

    '''Get search results'''
    result = requests.get(url)
    result.raise_for_status()

    '''Retrieve top search result links'''
    soup = bs4.BeautifulSoup(result.text, 'html.parser')

    project_link_tags = soup.select('a.package.snippet')
    print(f'Found {len(project_link_tags)} projects to open.')

    '''Open browser tab for each result'''
    num_links = min(args.num_links, len(project_link_tags))
    print(f'     ... opening {num_links}')

    for i in range(num_links):
        tag = project_link_tags(i)
        project_url = get_project_url(tag.get('herf'))
        print('Opening URL:', project_url)
        webbrowser.open(project_url)

if __name__ == '__main__':
    main()
