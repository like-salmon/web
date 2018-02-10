#!/usr/bin/python
# coding:utf-8

from pyexcel_xlsx import get_data
import random, re, os, time, urllib2
import json
import mysql.connector
from mysql.connector import errorcode
import hashlib

ds = {
    "host": 'localhost',
    'port': 3306,
    'user': 'root',
    'db': 'llidc',
    'passwd': "zxgj0313",
    'buffered': True,  # debug,some error accurs during processing data
    'charset': 'utf8',  # 默认即为utf8
}


def getran(n=5):
    a = []
    cset = [chr(i) for i in range(1, 256) if chr(i).isalnum()]  # alphabet or number
    for i in range(1, n + 1):
        a.append(random.choice(cset))
    return "".join(a)


def parser():
    f = get_data("D:\\mywork\\llidc\\script\\allmachines0818.xlsx")
    for i in f["dongguan"]:
        yield i


cnx = cur = None
c = 0
try:
    cnx = mysql.connector.connect(**ds)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    m = hashlib.md5()
    m.update("654321")
    npwd = m.hexdigest()
    print npwd
    csql = "select * from llidc_clients"
    cur.execute(csql)
    cs = cur.fetchall()
    print cs
    for i in cs:
        sql = "update llidc_clients set c_pwd = '%d' where c_id ='%s'"%(npwd,i[0])
        cur.execute(sql)
        c+=1



finally:
    if cur:
        cnx.commit()
        cur.close()
    if cnx:
        cnx.close()
    # print values
    print "共处理数据%d条." % c
    assert c > 0
    print "finished all"
