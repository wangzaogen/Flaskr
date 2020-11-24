from xy_sku_spider.db.db_utils import DBSession
from xy_sku_spider.db.db_utils import session_maker
from xy_sku_spider.item.haodf_keshi import HaoDfKeshi, HaoDfKeshiDoctorRel


def insert_keshi(keshi :HaoDfKeshi):
    session = DBSession()
    with session_maker(session) as db_session:
        add_user = keshi
        db_session.add(add_user)

def query_secondary_department_url(first_department):
    session = DBSession()
    with session_maker(session) as db_session:
        data = db_session.execute('''select id,first_department,secondary_department,secondary_department_url from xy_spider_haodf_keshi where first_department ='{0}'  '''.format(first_department))
        rows = data.fetchall()
        return rows

def query_department_info_by(secondary_department_url):
    session = DBSession()
    with session_maker(session) as db_session:
        data = db_session.execute('''select id,first_department,secondary_department,secondary_department_url from xy_spider_haodf_keshi where secondary_department_url ='{0}' limit 1  '''.format(secondary_department_url))
        row = data.fetchone()
        return row

def update_keshi(name):
    session = DBSession()
    with session_maker(session) as db_session:
        db_session.query(HaoDfKeshi).filter_by(id=1).update({'update_by': name})

def install_keshi_doctor_batch(keshi_doctors: list):
    session = DBSession()
    with session_maker(session) as db_session:
        db_session.add_all(keshi_doctors)

def install_keshi_doctor_rel(keshi_doctors: HaoDfKeshiDoctorRel):
    session = DBSession()
    with session_maker(session) as db_session:
        db_session.add(keshi_doctors)

if __name__ == '__main__':
    # query_secondary_department_url('内科')
    keshi = HaoDfKeshi('test','test','test')
    insert_keshi(keshi)