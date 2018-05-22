#!/usr/bin/env python
# encoding: utf-8
import requests
from bs4 import BeautifulSoup
from getapplist import xClientSite

def get_download_page(url, referer):
    # get this page will redirect to app intro page
    # guess: set referer field
    r = requests.get(url, headers={'referer': referer})
    soup = BeautifulSoup(r.content, "html.parser")
    link = soup.find('a', class_='btn_down_link pop_btn')
    disk_url = link.get('data-link')
    print(disk_url)
    disk_pass = link.get('data-clipboard-text')
    print(disk_pass)

def get_app_page(url):
    id = xClientSite().get_id()
    url += id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    links = soup.findAll('a', class_='btn-download')
    download_url_list = [link.get('href') for link in links if u'百度云盘' in link.text]

    for one_url in download_url_list:
        get_download_page(one_url, url)

if __name__ == '__main__':
    get_app_page('http://xclient.info/s/typinator.html')
