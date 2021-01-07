import os
import time
import json
import requests
import datetime
import traceback
from threading import Thread
from flask_cors import cross_origin
from flask import render_template, session, redirect, url_for, current_app, flash, request, jsonify
# from config_helper import ConfigHelper

# from . import news


NEWS_JSON_PATH = 'D:/wang_space/Flaskr' + '/news/json'
# DOMAIN_NAME = ConfigHelper().get('DOMAIN_NAME')
LIMITER_FREQUENCY_NEWS_GET = '10/minute'  # 接口限制的新闻获取访问频次
LIMITER_FREQUENCY_NEWS_FLUSH = '10/hour'  # 接口限制的新闻刷新访问频次


class MyThread(Thread):

    def __init__(self, target, args=()):
        super(MyThread, self).__init__()
        self.target = target
        self.args = args

    def run(self):
        self.result = self.target(*self.args)


# @news.route('/news_page', methods=['GET', 'POST'])
# def get():
#     try:
#         temp = {}
#         r = []
#         files = os.listdir(NEWS_JSON_PATH)
#         for file in files:
#             file_path = os.path.join(NEWS_JSON_PATH, file)
#             temp[file] = json.load(open(file_path))
#         r.append({'title': '百度', 'data': [temp.pop('baidu_now.json'), temp.pop('baidu_today.json'), temp.pop('baidu_week.json')]})
#         r.append({'title': '什么值得买', 'data': [temp.pop('smzdm_article_today.json'), temp.pop('smzdm_article_week.json'), temp.pop('smzdm_article_month.json')]})
#         r.append({'title': '知乎', 'data': [temp.pop('zhihu_daily.json'), temp.pop('zhihu_good.json'), temp.pop('zhihu_hot.json')]})
#         r.append({'title': '微信', 'data': [temp.pop('weixin_hot.json'), temp.pop('weixin.json')]})
#         r.append({'title': '36Kr', 'data': [temp.pop('36kr_hot.json'), temp.pop('36kr_article.json')]})
#         r.append({'title': '新京报', 'data': [temp.pop('bjnews_suggestion.json'), temp.pop('bjnews_ranking.json'), temp.pop('bjnews_comment_ranking.json')]})
#         r.append({'title': '黑客派', 'data': [temp.pop('hacpai_hot.json'), temp.pop('hacpai_play.json')]})
#
#         for key in temp:
#             r.append({'title': temp[key]['title'], 'data': [temp[key]]})
#
#         return render_template('news_page.html', news_info=r)
#     except Exception as e:
#         traceback.print_exc()


def news_page():
    try:
        temp = {}
        r = []
        files = os.listdir(NEWS_JSON_PATH)
        for file in files:
            file_path = os.path.join(NEWS_JSON_PATH, file)
            temp[file] = json.load(open(file_path,'r', encoding='UTF-8'), encoding='utf-8')
        # r.append({'title': '百度', 'data': [temp.pop('baidu_now.json'), temp.pop('baidu_today.json'), temp.pop('baidu_week.json')]})
        # r.append({'title': '什么值得买', 'data': [temp.pop('smzdm_article_today.json'), temp.pop('smzdm_article_week.json'), temp.pop('smzdm_article_month.json')]})
        # r.append({'title': '知乎', 'data': [temp.pop('zhihu_daily.json'), temp.pop('zhihu_good.json'), temp.pop('zhihu_hot.json')]})
        # r.append({'title': '微信', 'data': [temp.pop('weixin_hot.json'), temp.pop('weixin.json')]})
        # r.append(temp['36kr_hot.json']['data'])
        # r.append({'title': '新京报', 'data': [temp.pop('bjnews_suggestion.json'), temp.pop('bjnews_ranking.json'), temp.pop('bjnews_comment_ranking.json')]})
        # r.append({'title': '黑客派', 'data': [temp.pop('hacpai_hot.json'), temp.pop('hacpai_play.json')]})

        # for key in temp:
        #     r.append({'title': temp[key]['title'], 'data': [temp[key]]})

        print(temp['36kr_hot.json']['data'])
    except Exception as e:
        traceback.print_exc()


if __name__ == '__main__':
    news_page()


