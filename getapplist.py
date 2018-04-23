#!/usr/bin/env python
# encoding: utf-8
import requests
from bs4 import BeautifulSoup

class XclientSite(object):
    __id = ''
    def get_id(self):
        r = requests.get('http://xclient.info/s/', allow_redirects=False)
        self.__id = r.headers['location']
        return self.__id

    def get_app_list(self):
        url = 'http://xclient.info/s/' + self.get_id()
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        return [self.store_app_item(li) for li in soup.findAll("li", class_="col-6 col-4-m col-3-l col-2-xl")]

    def store_app_item(self, item):

        app = XclientApp()

        main = item.find("div", class_="main")
        app.name = main.a.get('title')
        app.addr = main.a.get('href')
        app.icon = main.a.img.get('src')

        status_bar = main.find("div", class_="status_bar")
        download = status_bar.find("span", class_="item download")
        date = status_bar.find("span", class_="item date")
        app.download_count = download.text
        app.update_date = date.text

        info = main.find("div", class_="info")
        app.description_title = info.h3.text
        app.description_detail = info.p.text

        cates = main.find("div", class_="cates")
        app.category = cates.a.text
        app.category_url = cates.a.get('href')

        return app

class XclientApp(object):
    name = ''
    addr = ''
    icon = ''
    download_count = 0
    update_date = ''
    description_title = ''
    description_detail = ''
    category = ''
    category_url = ''

    def __str__(self):
        return '\n'.join([
            'app',
            'name :{0}'.format(self.name),
            'addr :{0}'.format(self.addr),
            'icon :{0}'.format(self.icon),
            'download times :{0}'.format(self.download_count),
            'update date :{0}'.format(self.update_date),
            'title :{0}'.format(self.description_title),
            'description :{0}'.format(self.description_detail),
            'category :{0}'.format(self.category)]
        )

if __name__ == '__main__':
    list = XclientSite().get_app_list()
    for app in list:
        print(app)
