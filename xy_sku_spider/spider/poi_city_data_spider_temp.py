from xy_sku_spider.dao.poi_city_dao import update_poi_city, query_poi_city_by_page, query_poi_city_by_page_temp
from xy_sku_spider.item.poi_city_data import PoiCityData
from xy_sku_spider.request.proxy import get_random_proxy
from xy_sku_spider.response.response_result import get_soup
from xy_sku_spider.spider.base_spider import BaseSpider
import time
import threading
import traceback
import re

from xy_sku_spider.utility.writer import write_str_to_dfile

# loggings = Loggings('poiCity')
site = 'https://poi.mapbar.com/'

class PoiCityDataSpider(BaseSpider):

    def get_city_info(self, poi_city_id, url):
        print('爬取url:{0}--------------->start '.format(url))
        try:
            poi_city = PoiCityData()
            soup = get_soup(site, None, url)
            ul = soup.find('ul',class_='POI_ulA')
            if ul == None:
                print('爬取url:{0}--------------->未获取到数据 '.format(url))
                return
            lis = ul.find_all('li')
            tag_a = lis[1].find_all('a')
            poi_city.id = poi_city_id
            poi_city.area = '' if len(tag_a) <= 1 else tag_a[1].text.strip()
            address_array = str(lis[1].text.strip()).split(' ')
            poi_city.adress = address_array.pop(len(address_array)-1).strip()
            poi_city.tel_num = str(lis[2].text.strip()).replace('我来添加','')
            update_poi_city(poi_city)
            print('爬取url:{0}--------------->end '.format(url))
        except Exception as e:
            print("************get_city_info error:{0}，url:{1}".format(e, url))
            write_str_to_dfile('error_poiCity_urls.txt', url)
            traceback.print_exc()

    def start(self, size):
        for index in range(1, size):
            print('爬取页码：{0}-----------------'.format(index))
            rows = query_poi_city_by_page_temp(index, 10)
            threads = []
            for row in rows:
                thread = threading.Thread(target=self.get_city_info, args=[row[0], row[1]])
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()


if __name__ == '__main__':
    try:
        poi = PoiCityDataSpider('poi_city')
        time_start=time.time()
        poi.start(20000)
        print('爬取结束，执行时间：{}'.format(time.time() - time_start))
    except Exception as e:
        f = open("D:\\spider_error.txt", "w")
        traceback.print_exc(file=f)
        print(e)

