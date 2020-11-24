from xy_sku_spider.dao.taoshu_hospital_dao import install_hospital_batch
from xy_sku_spider.item.taoshu_hospital import TaoShuHospital
from xy_sku_spider.response.response_result import get_soup
from xy_sku_spider.spider.base_spider import BaseSpider
from xy_sku_spider.utility.log_print import Loggings
import time
import threading
import traceback

from xy_sku_spider.utility.writer import write_str_to_dfile

loggings = Loggings('taoshu_hospital')
site = 'http://taoshu.com.cn/'
hospital_url = 'http://taoshu.com.cn/hospital?page=1'

class TaoShuHospitalSpider(BaseSpider):

    def get_hospital_info(self, url):
        loggings.info('爬取url:{0}--------------->start '.format(url))
        try:
            soup = get_soup(site, None, url)
            table = soup.find('table', class_='layui-table')
            if table == None:
                return
            hospital_list = []
            for tr in table.find_all('tr')[1::]:
                hospital = TaoShuHospital()
                tds = tr.find_all('td')[1::]
                hospital.name = tds[0].text.strip()
                hospital.url = tds[0].find('a')['href']
                hospital.province = tds[1].text.strip()
                hospital.city = tds[2].text.strip()
                hospital.business_pattern = tds[3].text.strip()
                hospital.hospital_type = tds[4].text.strip()
                hospital.grade = tds[5].text.strip()
                hospital.department = tds[6].text.strip()
                hospital.outpatient = tds[7].text.strip()
                hospital.bed_numeric = tds[8].text.strip()
                hospital.phone = tds[9].text.strip()
                hospital.address = tds[10].text.strip()
                hospital.health_care = tds[11].text.strip()
                hospital.email = tds[12].text.strip()
                hospital.create_by = 'spider'
                hospital_list.append(hospital)
            install_hospital_batch(hospital_list)
        except Exception as e:
            loggings.error("************get_hospital_info error:{0}，url:{1}".format(e, url))
            write_str_to_dfile('error_hospital_page_urls.txt', url)
            traceback.print_exc()


    def batch_start(self, begin, end):
        url_list = []
        for index in range(begin, end):
            url_list.append('http://taoshu.com.cn/hospital?page={0}'.format(index))

        threads = []
        for url in url_list:
            thread = threading.Thread(target=self.get_hospital_info, args=[url])
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()






if __name__ == '__main__':
    taoshu = TaoShuHospitalSpider('taoshu')
    time_start=time.time()
    for index in range(3,470):
        loggings.info('爬取的页面范围，begin={}, end= {}'.format(index*10, index*10+10))
        taoshu.batch_start(index*10, index*10+10)

    loggings.info('爬取结束，执行时间：{}'.format(time.time() - time_start))


