from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,Integer

class PoiCityData(declarative_base()):

    __tablename__ = 'xy_spider_poi_city'
    id = Column(Integer, primary_key=True)
    city_url = Column(String(200))
    area = Column(String(200))
    adress = Column(String(1000))
    tel_num = Column(String(200))

