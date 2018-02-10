#!/usr/bin/python
#coding:utf-8

from pyexcel_xlsx import get_data
import random,re,os,time,urllib2
import json
import mysql.connector
from mysql.connector import errorcode
import hashlib

ds={
"host":'localhost',
'port':3306,
'user':'root',
'db':'llidc',
'passwd':"zxgj0313",
'buffered':True,#debug,some error accurs during processing data
'charset':'utf8',#默认即为utf8  
}


def getran(n=5):
    a = []
    cset = [chr(i) for i in range(1, 256) if chr(i).isalnum()]#alphabet or number
    for i in range(1, n + 1):
        a.append(random.choice(cset))
    return "".join(a)
    
def parser():
    f = get_data("D:\\mywork\\llidc\\script\\allmachines0818.xlsx")
    for i in f["dongguan"]:
        yield i

cnx = cur = None
c=0
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
    for a in parser():
        j=[]
        for k in a:
            if k:
                if isinstance(k,unicode):
                    j.append(k.encode("utf-8").strip())
                else:
                    j.append(str(k).strip())
            else:
                j.append("")
        #llidc_machines
        print j,len(j)
        values = (j[4],j[0],j[1],j[2],j[3],j[5],j[6],j[8],j[7],j[9],j[10],"0")
        #blade machine
        #sql = "insert into llidc_machines (m_ip,m_idc_location,m_cabinet_num,m_bm_num,m_bm_mnum,m_bm_ip,m_config,m_bandwidth,m_sales,m_memo,m_client,m_status,m_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql = "insert into llidc_machines (m_ip,m_idc_location,m_cabinet_num,m_num,m_num_wy,m_config,m_bandwidth,m_sales,m_memo,m_client,m_status,m_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,values)
        c+=1
        print "inserted values:",values
    """
    sql="SELECT * FROM llidc_orders o JOIN llidc_clients c ON o.o_client_id = c.c_acc JOIN llidc_machines m ON m.m_ip = o.o_ip"
    cur.execute(sql)
    rs = cur.fetchall()
    t = []
    k = set()
    print len(t)
    for a in rs:
        t.append(a[1].strip())
    print len(t)
    print len(rs)
        
    for i in parser():
        if i[1].strip() not in t:
            k.add(i[1].strip())
    for l in k:
        c+=1
        print l


    a=["劳兴华","陶秋梅","唐晓珍","黄小恩","廖超"]
    for i in a:
        pwd = getran(8)
        print pwd
        m= hashlib.md5()
        m.update(pwd+"llidc")
        npwd=m.hexdigest()
        values = ("llidc-"+getran(2),i,npwd,5 if i=="劳兴华" else 1)
        print values
        sql = "insert into llidc_employees (u_acc,u_name,u_pwd,u_type) values(%s,%s,%s,%s)"
        c+=1
    """

    
    """
    llidc_orders
    csql = "select c_acc from llidc_clients where c_real_name = '%s'"%j[0]
    print "当前用户姓名是:",j[0]
    cur.execute(csql)
    rs = cur.fetchone()
    values = (j[1].split(" ")[0], rs[0].strip() if rs else "",j[4],j[2],j[3],j[5])
    print rs
    print "当前用户账号是:",rs[0]
    sql = "insert into llidc_orders (o_ip,o_client_id,o_payment,o_start_datetime,o_expire_datetime,o_sales) values(%s,%s,%s,%s,%s,%s)
    """
    #llidc_machines 
    #values = (j[4],"1,厦门哈曼尼",j[1],j[2],j[3],j[5],j[6],j[7],j[8],j[9],j[10],"0")
    #sql = "insert into llidc_machines (m_ip,m_idc_location,m_cabinet_num,m_num,m_num_wy,m_config,m_bandwidth,m_sales,m_memo,m_client,m_status,m_type)"

    #刀片机
    #sql = "insert into llidc_machines (m_ip,m_idc_location,m_cabinet_num,m_bm_mnum,m_bm_ip,m_config,m_bandwidth,m_memo,m_sales,m_status,m_type)
    #values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #修改id
    """
    qsql = "select com_id from llidc_commission"
    cur.execute(qsql)
    ms = cur.fetchall()
    c = 620170800
    for i in ms:
        sql = "update llidc_commission set com_id = '%d' where com_id ='%s'"%(c,i[0])
        cur.execute(sql)
        c+=1
    """
    """llidc_clients
    #values = (getran(8),getran(6),j[0],j[1],j[3],j[2])
    #sql = "insert into llidc_clients (c_acc,c_pwd,c_name,c_real_name,c_id_card,c_belongsto) values(%s,%s,%s,%s,%s,%s)
    cur.execute(sql,values)
    c+=1
    print "inserted values:",values
    """
    
        
finally:
    if cur:
        cnx.commit()
        cur.close()
    if cnx:
        cnx.close()
    #print values
    print "共处理数据%d条."%c
    assert c>0
    print "finished all"
