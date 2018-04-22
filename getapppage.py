#!/usr/bin/env python
# encoding: utf-8
import requests
from bs4 import BeautifulSoup

def get_download_page(url):
    # get this page will redirect to app intro page
    # guess: set referer field
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup.prettify())

def get_app_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.findAll('a', class_='btn-download')
    download_url_list = [link.get('href') for link in links if u'百度云盘' in link.text]

    print(download_url_list)

    get_download_page(download_url_list[0])

if __name__ == '__main__':
    page = get_app_page('http://xclient.info/s/typinator.html')
    print(page)
