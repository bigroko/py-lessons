# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

URL_BASH = "http://bash.im/"
URL_BASH_PAGE = URL_BASH + "index/{}"


def get_all_quotes(num_pages=1):
    i = 1
    page_last_index = 0
    while i <= num_pages:
        if page_last_index == 0:
            bs = get_page_bs(get_page_source())
            page_last_index = int(get_page_last_index(bs))
            get_quotes(bs)
        else:
            bs = get_page_bs(get_page_source(
                                url=URL_BASH_PAGE.format(page_last_index - 1)))
            get_quotes(bs)
        i += 1


def get_quotes(bs):
    for item_name in bs.findAll('div', {'class': 'quote'}):
        print(item_name.string)


def get_page_last_index(bs):
    return bs.find('input', {'class': 'page'}).get("value")


def get_page_bs(source):
    return BeautifulSoup(source, "html.parser")


def get_page_source(url=URL_BASH):
    return requests.get(url).text


class Quote(object):
    def __init__(self, q_id, q_text, q_date, q_rate):
        self.q_id = q_id
        self.q_text = q_text
        self.q_date = q_date
        self.q_rate = q_rate


def main():
    pass

if __name__ == '__main__':
    main()
