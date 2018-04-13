#!/usr/bin/python
# coding: utf-8
import webbrowser as web
import os


def run_to_use_default_browser_open_url(url):
    web.open_new_tab(url)
    print 'run_to_use_default_browser_open_url  open url ending ....'


def browser_test():
    os.system('python -m SimpleHTTPServer 8080 &')
    url = 'http://0.0.0.0:8080'
    run_to_use_default_browser_open_url(url)


if __name__ == '__main__':
    browser_test()