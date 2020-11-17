from xy_sku_spider.utility.path import *


def read_list_for_file(file_name)  -> list:
    read_rs = []
    file_name = DATA_PATH + "\\" + file_name
    with open(file_name) as f:
        lines = f.readlines()
    for line in lines:
        read_rs.append(line.strip())

    return read_rs


def read_list_for_dfile(file_name)  -> list:
    read_rs = []
    file_name = 'D:' + "\\" + file_name
    with open(file_name) as f:
        lines = f.readlines()
    for line in lines:
        read_rs.append(line.strip())

    return read_rs

def read_str_for_file(file_name)  -> str:
    # jsdata = ''
    file_name = DATA_PATH + "\\" + file_name
    with open(file_name,'rb') as f:
        jsdata = f.read()
        return jsdata