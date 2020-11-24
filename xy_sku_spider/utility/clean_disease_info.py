import traceback

from bs4 import BeautifulSoup

from xy_sku_spider.dao.ask_cate_dao import query_disease_info_by, install_disease_clean_info, \
    query_disease_url_list_by_page
from xy_sku_spider.item.ask_cate import AskDiseaseCleanInfo
import threading

from xy_sku_spider.utility.list_util import split_list
from xy_sku_spider.utility.reader import read_list_for_dfile
from xy_sku_spider.utility.writer import write_str_to_dfile


def clean_info_yybk(row: tuple, diseaseCleanInfo: AskDiseaseCleanInfo):
    if row[2] != 'yybk':
        return
    soup = BeautifulSoup(row[3], "lxml")
    lis = soup.find_all('li')
    diseaseCleanInfo.department = str(lis[0].text).split('：')[1]
    diseaseCleanInfo.symptom = str(lis[1].text).split('：')[1]
    diseaseCleanInfo.crowd = str(lis[2].text).split('：')[1]
    diseaseCleanInfo.check = str(lis[3].text).split('：')[1]
    diseaseCleanInfo.cause_disease = str(lis[4].text).split('：')[1]
    diseaseCleanInfo.therapeutic_method = str(lis[5].text).split('：')[1]

def clean_info_jyxts(row: tuple, diseaseCleanInfo: AskDiseaseCleanInfo):
    if row[2] != 'jyxts':
        return
    soup = BeautifulSoup(row[3], "lxml")
    lis = soup.find_all('li')

    diseaseCleanInfo.common_drugs = str(lis[0].text).split('：')[1]
    diseaseCleanInfo.treatment_costs = str(lis[1].text).split('：')[1]
    diseaseCleanInfo.is_contagious = str(lis[2].text).split('：')[1]
    diseaseCleanInfo.prevalence_rate = str(lis[3].text).split('：')[1]
    diseaseCleanInfo.cure_rate = str(lis[4].text).split('：')[1]
    diseaseCleanInfo.treatment_cycle = str(lis[5].text).split('：')[1]

def install_info(url):
    print(f'正在清理url = {url}的数据----------------->start')
    try:
        diseaseCleanInfo = AskDiseaseCleanInfo()
        rows = query_disease_info_by(url)
        if len(rows) == 0:
            return
        diseaseCleanInfo.disease_name = rows[0][0]
        diseaseCleanInfo.disease_url = rows[0][1]
        diseaseCleanInfo.create_by = 'spider'
        clean_info_jyxts(rows[0], diseaseCleanInfo)
        clean_info_yybk(rows[1], diseaseCleanInfo)
        install_disease_clean_info(diseaseCleanInfo)
    except Exception as e:
        print("************diseaseCleanInfo error:{0}，url:{1}".format(e, url))
        write_str_to_dfile('error_diseaseCleanInfo_urls.txt', url)
        traceback.print_exc()
    print(f'正在清理url = {url}的数据----------------->end')

def start(size):
    for index in range(1, size):
        rows = query_disease_url_list_by_page(index, 100)
        for spilt_rows in split_list(rows, 10):
            threads = []
            for spilt_row in spilt_rows:
                thread = threading.Thread(target=install_info, args=[spilt_row[0]])
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join()

def start_by_file():
    urls = read_list_for_dfile('disease_url.txt')
    for url in urls:
        install_info(url)


if __name__ == '__main__':
    start_by_file()






