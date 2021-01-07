from flask import Flask, request,g, session, redirect, url_for, abort, \
    render_template, flash
import db_option
import translators as ts
import os
import time
import json
import requests
import datetime
import traceback

from config_helper import ConfigHelper

NEWS_JSON_PATH = ConfigHelper().get('BASE_PATH') + '/news/json'

app = Flask(__name__)
app.config['USERNAME'] = 'demo'
app.config['PASSWORD'] = '1234'
app.secret_key = 'wang'

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.before_request
def before_request():
    g.db = db_option.get_db()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/translator_en', methods=['GET', 'POST'])
def translator_en():
    result = None
    if request.method == 'POST':
        if request.form['translator_info'] != '':
            error = 'null'
        translator_info = request.form['translator_info']
        if is_contains_chinese(translator_info):
            result = ts.alibaba(translator_info, to_language='en', professional_field='general')
        else:
            result = ts.alibaba(translator_info, to_language='zh', professional_field='general')

    return render_template('fanyi.html', error=result)

@app.route('/news_page', methods=['GET', 'POST'])
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
        # r.append({'title': '36Kr', 'data': [temp.pop('36kr_hot.json'), temp.pop('36kr_article.json')]})
        # r.append({'title': '新京报', 'data': [temp.pop('bjnews_suggestion.json'), temp.pop('bjnews_ranking.json'), temp.pop('bjnews_comment_ranking.json')]})
        # r.append({'title': '黑客派', 'data': [temp.pop('hacpai_hot.json'), temp.pop('hacpai_play.json')]})
        #
        # for key in temp:
        #     r.append({'title': temp[key]['title'], 'data': [temp[key]]})

        return render_template('news_page.html', news_info=temp['36kr_hot.json']['data'])
    except Exception as e:
        traceback.print_exc()


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

if __name__ == '__main__':
    app.run()
