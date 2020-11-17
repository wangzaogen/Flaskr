from xy_sku_spider.spider.base_spider import BaseSpider
import random
import time
from xy_sku_spider.response.response_result import get_soup_gbk
from xy_sku_spider.item.haodf_keshi import HaoDfKeshi
from xy_sku_spider.utility.log_print import Loggings
from xy_sku_spider.dao.haodf_keshi_dao import insert_keshi

loggings = Loggings('haodf_keshi')

class HaoDfKeshiSpider(BaseSpider):

    def get_keshi_info(self,url):
        loggings.info('爬取科室url:{}'.format(url))
        soup = get_soup_gbk('haodf',None, url)
        ct = soup.find_all('div', class_='ct')[1]
        title_div = ct.select('.m_title_green')
        keshi_div = ct.find_all('div', class_='m_ctt_green')
        for div_index in range(0, len(keshi_div)):
            title_name =  title_div[div_index].text
            loggings.info('{}，下的科室列表'.format(title_name))
            tag_a = keshi_div[div_index].find_all('a')
            for a in tag_a:
                name = a.text.strip()
                url = 'https://www.haodf.com{0}'.format(a['href'])
                loggings.info('二级科室：{0}， url:{1}'.format(name,url))
                # keishi = HaoDfKeshi(title_name, name, url)
                # insert_keshi(keishi)


if __name__ == '__main__':
    keshi = HaoDfKeshiSpider('haodf')
    keshi.get_keshi_info('https://www.haodf.com/keshi/list.htm')

