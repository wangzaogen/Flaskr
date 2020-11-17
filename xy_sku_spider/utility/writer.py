

from xy_sku_spider.utility.path import *


def write_str_to_file(file_name, string):
    file_name = DATA_PATH + "\\" + file_name
    with open(file_name, 'a+') as f:
        f.write(string+'\n')

def write_urls_to_file(file_name, urls):
    file_name = DATA_PATH + "\\" + file_name
    with open(file_name, 'a+') as f:
        for url in urls:
            f.write(url+'\n')

def write_str_to_dfile(file_name, string):
    file_name = 'D:' + "\\" + file_name
    with open(file_name, 'a+') as f:
        f.write(string+'\n')
