#!/usr/bin/env python
# Project: Log Analysis
# Udacity Full stack web developer nanodegeree program
# Owner: Sinan AlChalabi
# Creating requried View for the project

import psycopg2

DBNAME = "news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
# Popular Articles View to collect most populer articles using this query:
SQL = '''create or replace view populararticle as
       select articles.slug,count(log.path) as num
       from articles,log
       where log.path = concat ('/article/',articles.slug)
       group by articles.slug
       order by num desc;'''
c.execute(SQL)
# WrongPages to calculate error requestes per day using this query:
SQL = '''create or replace view wrongpage as
       select time::DATE,count(time::DATE) as num
       from log
       where status!='200 OK'
       group by time::DATE
       order by time::DATE;'''
c.execute(SQL)
# SuccessfulPages to calculate total requestes per day using this query:
SQL = '''create or replace view totalpage as
 select time::DATE,count(time::DATE) as num
 from log
 group by time::DATE
 order by time::DATE;'''
c.execute(SQL)
db.commit()
db.close()
