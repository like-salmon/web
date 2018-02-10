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


def parser(t):
    f = get_data(t)
    for i in f["Sheet1"]:
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
    cur = cnx.cursor()
    t1 = "D:\\mywork\\llidc\\script\\clients0824.xlsx"
    for a in parser(t1):
        j = []
        for k in a:
            if k:
                if isinstance(k, unicode):
                    j.append(k.encode("utf-8").strip())
                else:
                    j.append(str(k).strip())
            else:
                j.append("")
        #llidc_clients
        print j[3]
        csql = "select * from llidc_clients where c_id_card = '%s'"%j[3].strip()
        cur.execute(csql)
        cc = cur.fetchone()
        print cc
        ucsql = "update llidc_clients set c_acc = '%s' where c_acc = '%s'"%(j[0],cc[1])
        uosql = "update llidc_orders set o_c_acc = '%s' where o_c_acc = '%s'"%(j[0],cc[1])
        c+=1
        print "update sql;from %s to %s"%(cc[1],j[0])

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
