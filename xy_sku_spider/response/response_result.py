from xy_sku_spider.request.headers import create_headers_one, create_headers_referer
import requests
from bs4 import BeautifulSoup
import random
import time
from xy_sku_spider.request.proxy import get_random_proxy
from xy_sku_spider.utility.date import get_time_string

PRO_IPS = ['103.21.141.43:16816', '49.7.96.227:16816','49.7.96.232:16816',
           '110.76.185.162:16816', '106.58.210.50:16816', '36.103.242.231:16816', '42.81.136.193:16816',
           '222.84.252.182:16816', '124.225.201.183:16816', '49.7.96.252:16816', '49.7.97.11:16816', '49.7.97.7:16816',
           '36.26.77.55:16816', '139.9.250.230:16816', '116.63.187.80:16816', '36.26.77.55:16816',
           '103.45.149.223:16816', '103.45.147.94:16816', '103.45.147.21:16816',
           '118.244.206.143:16816', '218.241.17.128:16816', '218.241.17.140:16816', '122.114.197.70:16816',
           '122.114.125.90:16816', '122.114.102.175:16816', '116.255.197.14:16816', '122.114.148.187:16816']

def get_soup_gbk(header_host, proxies,url, sleep_time = 2) -> BeautifulSoup:
    time.sleep(sleep_time)
    headers = create_headers_one(header_host)
    response = requests.get(url, timeout=10, headers=headers,proxies=proxies)
    print("response.status_code:{0}".format(response.status_code))
    html = response.content
    return BeautifulSoup(html, "html.parser",fromEncoding='gb18030')


def get_soup(header_host, proxies,url, sleep_time = 2) -> BeautifulSoup:
    time.sleep(sleep_time)
    proxy_ip = random.choice(PRO_IPS)
    username = "xxxxx"
    password = "xxxxx"
    proxys = {'http': "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
              'https': "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}}
    headers = create_headers_referer(header_host)
    response = requests.get(url, timeout=10, headers=headers,proxies=proxys)
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