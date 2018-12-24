#!/usr/bin/env python
# Project: Log Analysis
# Udacity Full stack web developer nanodegeree program
# Owner: Sinan AlChalabi
# Analysing news web page logs

import psycopg2
from datetime import datetime

DBNAME = "news"

try:
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # Query to find the most popular three articles
    SQL = '''select articles.title,particle.num
             from articles,(select articles.slug as slug,count(log.path)
             as num from articles,log
             where log.path = concat ('/article/',articles.slug)
             group by articles.slug )
             as particle
             where articles.slug = particle.slug
             order by particle.num desc limit 3;'''
    c.execute(SQL)
    articles = c.fetchall()
    print("Question 1: What are the most \
	popular three articles of all time?\n")
    for art, num in articles:
        print '"', art, '"--', num, "Views"
    # Query to find the most popular authors
    SQL = '''select authors.name,popularauthor.pauthor
             from authors,
              (select articles.author as authorid,
               sum(populararticle.num) as pauthor
               from articles,populararticle
               where populararticle.slug = articles.slug
               group by articles.author)
               as popularauthor
               where popularauthor.authorid = authors.id
               order by popularauthor.pauthor desc;'''
    c.execute(SQL)
    authors = c.fetchall()
    print("\nQuestion 2: Who are the most \
    popular article authors of all time?\n")
    for auth, num in authors:
        print '"', auth, '"--', num, "Views"
    # Query to find days with more than 1% errors
    SQL = '''select * from \
               (select to_char(wrongpage.time, 'FMMonth DD, YYYY'),
               (cast(wrongpage.num as float)/cast(totalpage.num as float)*100)
                as ratio
                from totalpage,wrongpage
                where totalpage.time = wrongpage.time)
             as errorratio
             where ratio >1;'''
    c.execute(SQL)
    error = c.fetchall()
    print("\nQuestion 3: On which days did \
    more than 1% of requests lead to errors?\n")
    for date, err in error:
        print date, '--', err, "% errors"
    db.close()
except psycopg2.Error as erro:
    print "Unable to connect to database"
    print erro
    sys.exit(1)
