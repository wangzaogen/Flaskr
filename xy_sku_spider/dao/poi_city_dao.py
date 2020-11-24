from xy_sku_spider.db.db_utils import DBSession
from xy_sku_spider.db.db_utils import session_maker
from xy_sku_spider.item.poi_city_data import PoiCityData
from xy_sku_spider.utility.page_util import offset_current


def query_poi_city_by_page(page_index, page_size):
    offest = offset_current(page_index, page_size)
    session = DBSession()
    with session_maker(session) as db_session:
        data = db_session.execute('''select id,city_url from xy_spider_poi_city where id > 881135 ORDER BY id limit {0}, {1}  '''.format(offest, page_size))
        rows = data.fetchall()
        return rows

def query_poi_city_by_page_temp(page_index, page_size):
    offest = offset_current(page_index, page_size)
    session = DBSession()
    with session_maker(session) as db_session:
        data = db_session.execute('''select id,city_url from xy_spider_poi_city where id > 1081135 ORDER BY id limit {0}, {1}  '''.format(offest, page_size))
        rows = data.fetchall()
        return rows

def update_poi_city(poi_city : PoiCityData):
    session = DBSession()
    with session_maker(session) as db_session:
        db_session.query(PoiCityData).filter_by(id=poi_city.id).update({'area': poi_city.area,'adress': poi_city.adress,'tel_num': poi_city.tel_num})


if __name__ == '__main__':
    poi_city = PoiCityData()