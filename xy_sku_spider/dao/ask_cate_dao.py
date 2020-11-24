from xy_sku_spider.db.db_utils import DBSession
from xy_sku_spider.db.db_utils import session_maker
from xy_sku_spider.item.ask_cate import AskCate, AskDisease, AskDiseaseCleanInfo
from xy_sku_spider.utility.page_util import offset_current


def query_disease_url(cate_name) -> AskCate:
    cate = AskCate()
    session = DBSession()
    with session_maker(session) as db_session:
        askCate = db_session.query(AskCate).filter_by(cate_name=cate_name).one()
        cate.id = askCate.id
        cate.cate_url = askCate.cate_url
        cate.cate_name = askCate.cate_name
    return cate

def query_disease_url_list(parent_id) -> tuple:
    session = DBSession()
    with session_maker(session) as db_session:
        data = db_session.execute('''select id, cate_name, cate_url from xy_spider_120ask_cate where parent_id ={0} '''.format(parent_id))
        row = data.fetchall()
        return row

def query_disease_url_list_by_page(page_index, page_size) -> tuple:
    offest = offset_current(page_index, page_size)
    session = DBSession()
    with session_maker(session) as db_session:
        data = db_session.execute('''select cate_url from xy_spider_120ask_cate where level_num = 3 ORDER BY id limit {0}, {1} '''.format(offest, page_size))
        row = data.fetchall()
        return row

def install_disease(disease: AskDisease):
    session = DBSession()
    with session_maker(session) as db_session:
        add_user = disease
        db_session.add(add_user)

def query_disease_info(page_index, page_size):
    offest = offset_current(page_index, page_size)
    session = DBSession()
    with session_maker(session) as db_session:
        data = db_session.execute('''select id,cate_id,disease_name,disease_url,disease_tag,disease_tag_url, tag_context from xy_spider_120ask_jibing_details_bak ORDER BY id limit {0}, {1} '''.format(offest, page_size))
        row = data.fetchall()
        return row

def query_disease_info_by(disease_url):
    session = DBSession()
    with session_maker(session) as db_session:
        data = db_session.execute('''select disease_name,disease_url,disease_tag, tag_context from xy_spider_120ask_jibing_details_bak where disease_tag in ('jyxts','yybk') and disease_url = '{0}'  ORDER BY disease_tag'''.format(disease_url))
        row = data.fetchall()
        return row

def install_disease_clean_info(disease: AskDiseaseCleanInfo):
    session = DBSession()
    with session_maker(session) as db_session:
        db_session.add(disease)



if __name__ == '__main__':
    d = AskDisease('1','2','3','4','5','6')
    install_disease(d)