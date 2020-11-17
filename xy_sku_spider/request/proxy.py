
from bs4 import BeautifulSoup
import requests
from xy_sku_spider.request.headers import create_headers
from xy_sku_spider.utility.writer import write_str_to_file
from xy_sku_spider.utility.reader import read_list_for_file
import random

proxys_src = []
proxys = []
ip_address_file = "ip_adds.txt"


def spider_proxyip(page=2):
    try:
        for index in range(1,3):
            url = 'https://ip.jiangxianli.com/?page={0}&country=%E4%B8%AD%E5%9B%BD'.format(index)
            req = requests.get(url, headers=create_headers())
            source_code = req.content
            print(source_code)
            soup = BeautifulSoup(source_code, 'lxml')
            ips = soup.findAll('tr')

            for x in range(1, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                proxy_host = "{0}:{1}".format(tds[0].contents[0], tds[1].contents[0])
                if check_ip(tds[0].contents[0], tds[1].contents[0]):
                    write_str_to_file(ip_address_file, proxy_host)
                proxys_src.append(proxy_host)
    except Exception as e:
        print("spider_proxyip exception:")
        print(e)

def check_ip(ip, port):
    """测试IP地址是否有效"""
    ip_url = str(ip) + ':' + str(port)
    proxies = {'http': 'http://' + ip_url, 'https': 'https://' + ip_url}
    res = False
    try:
        request = requests.get('http://icanhazip.com/', headers=create_headers(), proxies=proxies, timeout=10)
        if request.status_code == 200:
            res = True
    except Exception as error_info:
        print('{0},IP地址是无效'.format(ip_url))
        res = False
    return res

def spider_proxyip_other():
    req = requests.get('http://kps.kdlapi.com/api/getkps/?orderid=920014954014068&num=30&sep=4', headers=create_headers())
    req.enconding = "utf-8"
    print(req.content)
    for ips in str(req.content).split('|'):
        if check_ip(ips.split(':')[0], ips.split(':')[1]):
            write_str_to_file(ip_address_file, ips)

    pass

def get_random_ip() -> dict:
    ips = read_list_for_file(ip_address_file)
    proxy_ip = random.choice(ips)
    proxies = {'http://': proxy_ip,'https://':proxy_ip}
    return proxies

def get_random_proxy() ->dict:
    ip = requests.get('http://10.6.14.30:5555/random').text.strip()
    return {'http://': ip,'https://':ip}





if __name__ == '__main__':
    proxy = {
        'ip':'106.58.210.50',
        'port':'16816'
    }
    # check_ip(proxy)
    # spider_proxyip(2)

    print(get_random_ip())
