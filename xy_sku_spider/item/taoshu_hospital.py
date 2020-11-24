from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,Integer


class TaoShuHospital(declarative_base()):
    __tablename__ = 'xy_spider_taoshu_hospital'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    url = Column(String(100))
    province = Column(String(200))
    city = Column(String(200))
    business_pattern = Column(String(200))
    hospital_type = Column(String(200))
    grade = Column(String(200))
    department = Column(String(2000))
    outpatient = Column(String(200))
    bed_numeric = Column(String(200))
    phone = Column(String(200))
    address = Column(String(2000))
    health_care = Column(String(200))
    email = Column(String(200))
    create_by = Column(String(20))

    # def __init__(self, name, url, province, city, business_pattern, grade, department, outpatient, bed_numeric, phone, address, health_care, email):
    #     self.name = name
    #     self.url = url
    #     self.province = province
    #     self.city = city
    #     self.business_pattern = business_pattern
    #     self.grade = grade
    #     self.department = department
    #     self.outpatient = outpatient
    #     self.bed_numeric = bed_numeric
    #     self.phone = phone
    #     self.address = address
    #     self.health_care = health_care
    #     self.email = email

