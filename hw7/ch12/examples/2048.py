#!/usr/bin/env/ python3
'''Automatically play a game'''
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''Will create a return selenium
broswer object that is navigated to the maze page'''
def get_browser():
    browser = webdriver.Firefox()
    browser.get(
        'https://gabrielecirulli.github.io/2048/'
    )
    return browser

def find_solution(browser):
    html = browser.find_element_by_tag_name('html')
    while True:
        keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

        html.send_keys(random.choice(keys))
        print('Game Over')
        browser.quit()
        return False

def main():
    browser = get_browser()
    find_solution(browser)

if __name__ == '__main__':
    main()
