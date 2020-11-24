import re
import threading
from xy_sku_spider.dao.ask_cate_dao import query_disease_info, install_disease
from xy_sku_spider.item.ask_cate import AskDisease
from xy_sku_spider.utility.list_util import split_list


def remove_a(target):
    c = re.compile('<a (.*?)>')
    ret = c.sub('', target)
    new_ret = ret.replace('</a>','')
    return new_ret

def install_no_atag(row: tuple):
    tag_context = remove_a(row[6])
    disease =  AskDisease(row[0],row[1],row[2],row[3],row[4],row[5],tag_context)
    print(f'disease_name:{row[2]},disease_tag:{row[4]}')
    install_disease(disease)


def start(size):
    for index in range(1, size):
        print('爬取页码：{0}-----------------'.format(index))
        rows = query_disease_info(index, 1000)
        threads = []
        for spilt_rows in split_list(rows, 10):
            for row in spilt_rows:
                thread = threading.Thread(target=install_no_atag, args=[row])
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

if __name__ == '__main__':
    start(116)