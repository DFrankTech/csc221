#!/usr/bin/env python3
# Built-in mods
import time
import random
# 3rd party mods
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''Will create a return selenium
broswer object that is navigated to the maze page'''
def get_browser():
    browser = webdriver.Firefox()
    browser.get(
        'https://www.goshdarngames.com/games-page-files/amaze/html5-maze/index.html'
    )
    return browser

def find_solution(browser, time_limit):
    '''Time limit in seconds'''
    html = browser.find_element_by_tag_name('html')
    keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

    start = time.time()
    while time.time() < (start + time_limit):
        html.send_keys(random.choice(keys))
    '''Kill browser screen if over time'''
    print('OVER TIME!!!!')
    browser.quit()
    return False

def main():
    '''Time limit 30 seconds'''
    browser = get_browser()
    find_solution(browser, 30)

if __name__ == '__main__':
    main()
