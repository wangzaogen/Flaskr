from xy_sku_spider.db.db_utils import DBSession
from xy_sku_spider.db.db_utils import session_maker
from xy_sku_spider.item.taoshu_hospital import TaoShuHospital


def install_hospital(hospital: TaoShuHospital):
    session = DBSession()
    with session_maker(session) as db_session:
        add_user = hospital
        db_session.add(add_user)

def install_hospital_batch(hospitals: list):
    session = DBSession()
    with session_maker(session) as db_session:
        db_session.add_all(hospitals)