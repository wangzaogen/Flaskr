from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,Integer

class HaoDfKeshi(declarative_base()):
    __tablename__ = 'xy_spider_haodf_keshi'
    id = Column(Integer, primary_key=True)
    first_department = Column(String(100))
    secondary_department = Column(String(100))
    secondary_department_url =  Column(String(500))
    create_by =  Column(String(50))
    update_by =  Column(String(50))

    def __init__(self, first_department, secondary_department,secondary_department_url):
        self.first_department = first_department
        self.secondary_department = secondary_department
        self.secondary_department_url = secondary_department_url
        self.create_by = 'spider'


