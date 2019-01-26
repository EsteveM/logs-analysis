#!/usr/bin/env python3
#
# Database code for the reporting tool that prints out reports based on the
# data in the DB News.

import psycopg2

DBNAME = "news"


def question_one():
    """Return what are the most popular three articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select articles.title, count(*) as views " +
              "from articles left join log " +
              "on concat('/article/', articles.slug) = log.path " +
              "group by articles.title " +
              "order by views desc " +
              "limit 3")
    articles = c.fetchall()
    db.close()
    return "\n".join("{} - \"{}\" - {} views".format((index + 1), article[0],
                                                     article[1])
                     for index, article in enumerate(articles))


def question_two():
    """Return who are the most popular article authors of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select authors.name, count(*) as views " +
              "from authors, articles, log " +
              "where authors.id = articles.author and " +
              "concat('/article/', articles.slug) = log.path " +
              "group by authors.name " +
              "order by views desc")
    authors = c.fetchall()
    db.close()
    return "\n".join("{} - {} - {} views".format((index + 1), author[0],
                                                 author[1])
                     for index, author in enumerate(authors))


def question_three():
    """Return which days more than 1% of requests led to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select subqtotal.time::date, " +
              "       round(((totalnok::numeric/total::numeric) * 100), 2) " +
              "from (select time::date, count(*) as total " +
              "      from log " +
              "      group by time::date) as subqtotal, " +
              "     (select time::date, count(*) as totalnok " +
              "      from log " +
              "      where status != '200 OK' " +
              "      group by time::date) as subqnok " +
              "where subqtotal.time::date = subqnok.time::date and" +
              "      ((totalnok::numeric/total::numeric) * 100) > 1 " +
              "order by subqtotal.time::date desc;")
    days = c.fetchall()
    db.close()
    return "\n".join("{} - {} - {}%".format((index + 1), day[0], day[1])
                     for index, day in enumerate(days))


print("\n1. What are the most popular three articles of all time?\n")
articles = question_one()
print(articles)
print("\n2. Who are the most popular article authors of all time?\n")
authors = question_two()
print(authors)
print("\n3. On which days did more than 1% of requests lead to errors?\n")
days = question_three()
print(days + "\n")
