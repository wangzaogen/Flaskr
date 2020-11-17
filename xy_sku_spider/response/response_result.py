from xy_sku_spider.request.headers import create_headers_one
import requests
from bs4 import BeautifulSoup
import random
import time
from xy_sku_spider.request.proxy import get_random_proxy
from xy_sku_spider.utility.date import get_time_string

def get_soup_gbk(header_host, proxies,url, sleep_time = 2) -> BeautifulSoup:
    time.sleep(sleep_time)
    headers = create_headers_one(header_host)
    response = requests.get(url, timeout=10, headers=headers,proxies=proxies)
    print("response.status_code:{0}".format(response.status_code))
    html = response.content
    return BeautifulSoup(html, "html.parser",fromEncoding='gb18030')


def get_soup(header_host, proxies,url, sleep_time = 2) -> BeautifulSoup:
    time.sleep(sleep_time)
    headers = create_headers_one(header_host)
    response = requests.get(url, timeout=10, headers=headers,proxies=proxies)
    print("response.status_code:{0}".format(response.status_code))
    html = response.content
    return BeautifulSoup(html, "lxml")

def do_request(header_host :str, url :str, count :int):
    proxies = random.choice([get_random_proxy(),None])
    headers = create_headers_one(header_host)
    response = requests.get(url, timeout=10, headers=headers, proxies=proxies)
    if response.status_code != 200 and count < 6:
        time.sleep(2)
        response=do_request(url,count + 1)
    print("日期：{} ,代理:{},请求返回:{}".format(get_time_string(),str(proxies),response.status_code))
    return response