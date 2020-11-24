from xy_sku_spider.dao.ask_cate_dao import install_disease, query_disease_url_list
from xy_sku_spider.item.ask_cate import AskDisease
from xy_sku_spider.response.response_result import get_soup
from xy_sku_spider.spider.base_spider import BaseSpider
from xy_sku_spider.utility.log_print import Loggings
from gevent.pool import Pool
import time
import threading

tags = ['gaishu','bingyin','zhengzhuang','jiancha','jianbie','bingfa','yufang','zhiliao','yinshi','shiliao']

loggings = Loggings('120ask_disease')

site = 'https://tag.120ask.com/'

class AskDiseaseSpider(BaseSpider):

    def get_disease_info_batch(self,row:tuple):
        loggings.info('爬取疾病url:{}，start ......'.format(row[2]))
        pool = Pool(len(tags))
        for tag in tags:
            pool.spawn(self.get_tag_info, row, tag)
        pool.join()

    def get_disease_info(self,row:tuple):
        loggings.info('爬取疾病url:{}，start ......'.format(row[2]))
        for tag in tags:
            self.get_tag_info(row ,tag)

    def get_disease_info_threading(self,row:tuple):
        loggings.info('爬取疾病url:{}，start ......'.format(row[2]))
        threads = []
        for tag in tags:
            thread = threading.Thread(target=self.get_tag_info, args=[row ,tag])
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

        loggings.info('爬取疾病url:{}，end ......'.format(row[2]))


    def get_tag_info(self,row:tuple, tag):
        tag_url = row[2]+tag
        loggings.info('爬取疾病tag url:{}，start ......'.format(tag_url))
        soup = get_soup(site, None, row[2]+tag)
        art_cont_div = None
        if tag == 'shiliao':
            art_cont_div = soup.find('div', class_='wrap_big')
        else:
            art_cont_div = soup.find('div', class_='art_cont')
        tag_context = str(art_cont_div)
        disease_info = AskDisease(row[0], row[1], row[2], tag, tag_url, tag_context)
        install_disease(disease_info)

    def start(self, parent_id):
        rows = query_disease_url_list(parent_id)
        for row in rows:
            self.get_disease_info(row)


if __name__ == '__main__':
    ask = AskDiseaseSpider('120ask')
    time_start=time.time()
    ask.get_disease_info(('4160','c胰岛功能性β细胞瘤','http://tag.120ask.com/jibing/cydgnxβxbl/'))
    print('执行时间：{}', time.time() - time_start)

