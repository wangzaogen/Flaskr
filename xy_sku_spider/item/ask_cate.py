from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,Integer,Text

class AskCate(declarative_base()):
    __tablename__ = 'xy_spider_120ask_cate'
    id = Column(Integer, primary_key=True)
    cate_name = Column(String(200))
    cate_url = Column(String(200))

    # def __init__(self, id, cate_name, cate_url):
    #     self.id = id
    #     self.cate_name = cate_name
    #     self.cate_url = cate_url

class AskDisease(declarative_base()):
    __tablename__ = 'xy_spider_120ask_jibing_details'
    id = Column(Integer, primary_key=True)
    disease_name = Column(String(200))
    disease_url = Column(String(200))
    disease_tag = Column(String(200))
    disease_tag_url = Column(String(200))
    tag_context = Column(Text)
    create_by = Column(String(200))
    cate_id = Column(Integer)

    def __init__(self,id,cate_id, disease_name, disease_url, disease_tag, disease_tag_url, tag_context):
        self.id = id
        self.disease_name = disease_name
        self.disease_url = disease_url
        self.disease_tag = disease_tag
        self.disease_tag_url = disease_tag_url
        self.tag_context = tag_context
        self.cate_id = cate_id
        self.create_by = 'spider'

class AskDiseaseBak(declarative_base()):
    __tablename__ = 'xy_spider_120ask_jibing_details_bak'
    id = Column(Integer, primary_key=True)
    disease_name = Column(String(200))
    disease_url = Column(String(200))
    disease_tag = Column(String(200))
    disease_tag_url = Column(String(200))
    tag_context = Column(Text)
    create_by = Column(String(200))
    cate_id = Column(Integer)


class AskDiseaseCleanInfo(declarative_base()):
    __tablename__ = 'xy_spider_120ask_jibing_clean_info'
    id = Column(Integer, primary_key=True)
    disease_name = Column(String(200))
    disease_url = Column(String(200))
    department = Column(String(200))
    symptom = Column(String(200))
    crowd = Column(Text)
    check = Column(String(200))
    cause_disease = Column(String(200))
    therapeutic_method = Column(String(200))
    common_drugs = Column(String(200))
    treatment_costs = Column(String(200))
    is_contagious = Column(String(200))
    prevalence_rate = Column(String(200))
    cure_rate = Column(String(200))
    treatment_cycle = Column(String(200))
    create_by = Column(String(200))


