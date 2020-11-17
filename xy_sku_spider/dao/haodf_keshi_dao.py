from xy_sku_spider.db.db_utils import DBSession
from xy_sku_spider.db.db_utils import session_maker
from xy_sku_spider.item.haodf_keshi import HaoDfKeshi

def insert_keshi(keshi :HaoDfKeshi):
    session = DBSession()
    with session_maker(session) as db_session:
        add_user = keshi
        db_session.add(add_user)

def query_secondary_department_url(first_department):
    session = DBSession()
    with session_maker(session) as db_session:
        data = db_session.execute('''select * from xy_spider_haodf_keshi where first_department ='{0}' limit 1'''.format(first_department))
        row = data.fetchone()
        print(row.id)
        print(row.secondary_department_url)

def update_keshi(name):
    session = DBSession()
    with session_maker(session) as db_session:
        db_session.query(HaoDfKeshi).filter_by(id=1).update({'update_by': name})

if __name__ == '__main__':
    # query_secondary_department_url('内科')
    keshi = HaoDfKeshi('test','test','test')
    insert_keshi(keshi)