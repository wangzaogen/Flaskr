import traceback

from xy_sku_spider.spider.base_spider import BaseSpider
import random
import time
from xy_sku_spider.response.response_result import get_soup_gbk
from xy_sku_spider.item.haodf_keshi import HaoDfKeshi, HaoDfKeshiDoctorRel
from xy_sku_spider.utility.log_print import Loggings
from xy_sku_spider.dao.haodf_keshi_dao import insert_keshi, query_secondary_department_url, install_keshi_doctor_batch, \
    query_department_info_by, install_keshi_doctor_rel
import re
import threading

from xy_sku_spider.utility.reader import read_list_for_dfile
from xy_sku_spider.utility.writer import write_str_to_dfile

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

    def get_doctor_by_keshi(self, first_department):
        rows = query_secondary_department_url(first_department)
        for row in rows:
            pass


    def get_doctor_list(self, row:tuple):
        url = row[3]
        loggings.info('当前爬取的科室：{0}， url:{1}'.format(row[2],url))
        soup = get_soup_gbk('haodf',None, row[3])
        page_size = 1
        if soup.find('a', class_='p_text') != None:
            page_a = soup.find('a', class_='p_text').text.strip()
            page_size = int(re.findall(r"\d+\.?\d*",page_a)[0])
        loggings.info('当前爬取的医生总页数：{0}'.format(page_size))
        self.insert_info(soup, row,'')
        if page_size > 1:
            page_num = int(page_size /10) if page_size % 10 == 0 else page_size//10+1
            for index in range(0, page_num+1):
                page_list = [url.replace('.htm','_{0}.htm'.format(i))  for i in range(index*10, index*10+10) if i not in [0,1]]
                loggings.info(page_list)
                threads = []
                for page_url in page_list:
                    thread = threading.Thread(target=self.insert_info, args=[None,row, page_url])
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()


    def insert_info(self, soup, row:tuple, url):
        try:
            soup = soup if soup != None else get_soup_gbk('haodf',None, url)
            doctor_rels = []
            table = soup.find('table', class_='bluegpanel')
            doctor_trs = table.find_all('table')[2].find_all('table')
            for tr in doctor_trs:
                if len(tr.find_all('a', class_='blue')) == 0:
                    continue
                a_tag = tr.find_all('a', class_='blue')[0]
                doctor_rel = HaoDfKeshiDoctorRel()
                doctor_rel.keshi_id = row[0]
                doctor_rel.first_department = row[1]
                doctor_rel.secondary_department = row[2]
                doctor_url = a_tag['href']
                doctor_rel.doctor_url = doctor_url
                doctor_rel.doctor_name = a_tag.text.strip()
                doctor_rel.create_by = 'spider'
                doctor_rels.append(doctor_rel)

            install_keshi_doctor_batch(doctor_rels)
        except Exception as e:
            loggings.error("************get_doctor_list error:{0}，url:{1}".format(e, doctor_url))
            write_str_to_dfile('error_doctor_page_urls.txt', doctor_url)
            traceback.print_exc()


    def insert_error_info(self, soup, row:tuple, url):
        soup = soup if soup != None else get_soup_gbk('haodf',None, url)
        doctor_rels = []
        table = soup.find('table', class_='bluegpanel')
        doctor_trs = table.find_all('table')[2].find_all('table')

        for tr in doctor_trs:
            try:
                if len(tr.find_all('a', class_='blue')) == 0:
                    continue
                a_tag = tr.find_all('a', class_='blue')[0]
                doctor_rel = HaoDfKeshiDoctorRel()
                doctor_rel.keshi_id = row[0]
                doctor_rel.first_department = row[1]
                doctor_rel.secondary_department = row[2]
                doctor_url = a_tag['href']
                doctor_rel.doctor_url = doctor_url
                doctor_rel.doctor_name = a_tag.text.strip()
                doctor_rel.create_by = 'spider'
                doctor_rels.append(doctor_rel)
                install_keshi_doctor_rel(doctor_rel)

            except Exception as e:
                loggings.error("************get_doctor_list error:{0}，url:{1}".format(e, doctor_url))
                write_str_to_dfile('error_doctor_urls.txt', doctor_url)
                traceback.print_exc()

    def start(self, first_department):
        rows = query_secondary_department_url(first_department)
        for row in rows:
            self.get_doctor_list(row)

    def error_opt_start(self):
        error_pages = read_list_for_dfile('error_doctor_page_urls.txt')
        for url in error_pages:
            strs = url.split('/')
            strs.pop(len(strs)-1)
            strs.append('daifu_all.htm')
            secondary_department_url = '/'.join(strs)
            row = query_department_info_by(secondary_department_url)
            self.insert_error_info(None, row, url)






if __name__ == '__main__':
    keshi = HaoDfKeshiSpider('haodf')
    # dep_1 = ['妇产科学','生殖中心','儿科学','骨外科','眼科学','口腔科学','耳鼻咽喉头颈科']
    # dep_2 = ['肿瘤科','皮肤性病科','男科','皮肤美容','烧伤科','精神心理科']
    # dep_3 = ['中医学','中西医结合科','传染病科','结核病科','介入医学科']
    # dep_4 = ['康复医学科','运动医学科','麻醉医学科','职业病科','地方病科','营养科','医学影像学','病理科','其他科室']
    # time_start=time.time()
    # for dep in dep_4:
    #     keshi.start(dep)
    # loggings.info('爬取结束，执行时间：{}'.format(time.time() - time_start))
    keshi.error_opt_start()



