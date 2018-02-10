#!/usr/bin python
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

############################生成网站订单测试数据

cnx = cur = None
c=0
com_config = {"r":50,"s":30,"t":120,"u":120,"v":0.1,"w":0.1,"x":0.05,'k':0.1,'l':50}#对应 order_product_type和sub_order_type
renew_com_config = {"rr":25,"rs":20,"rt":80,"ru":80,"rv":0.1,"rw":0.1,"rx":0.03}#renew order,add bandwidth,add defence is not took into consideration
sid = []
financial_log = {"o":"续期"}
def getnum(cls,n=5):
    a = []
    cset = [chr(i) for i in range(1, 256) if chr(i).isdigit()]#alphabet or number
    for i in range(1, n + 1):
        a.append(random.choice(cset))
    return "".join(a)
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
    """
    esql = "insert into llidc_employees (u_id,u_acc,u_name,u_pwd) values(%s,%s,%s,%s)"
    values = ("24","test","测试","081e64abc7121cc0339b0b749bfa353f")#123456
    rs = cur.execute(esql,values)
    """
    #新增订单
    for i in xrange(2000):
        if i<1000:#主订单
            print "正在处理主订单",i
            oid = "llidc"+"-"+getnum(8)+str(int(str(int(time.time()))))+str(random.choice(range(50)))
            sid.append(oid) if i %2 ==0 else ""
            ip = "117.25.154.130"
            cacc = "test001"
            payment = random.choice(xrange(500))*i
            sd = "2017/06/09"
            expire = "2017/0"+str(random.choice([7,8,9,10,11,12]))+"/09"
            stype = "b,租用" if i%2 ==0 else "c,托管"
            ptype = "r,普通机托管" if i%2 == 0 else "s,普通机租用" if i % 3 == 0 else "t,高防机托管" if i%7 == 0 else "v,代理机托管" if i%11 == 0 else "x,机柜出租" if i%13 ==0 else "r,普通机托管"
            print ptype
            sql = "insert into llidc_orders (o_id,o_ip,o_c_acc,o_payment,o_start_datetime,o_expire_datetime,o_m_stype,o_ptype,o_sales,o_memo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            sales = "23,测试"
            memo = "主订单备注"
            values = (oid,ip,cacc,payment,sd,expire,stype,ptype,sales,memo)
            ors = cur.execute(sql, values)
            #新增财务流水
            #write to fiancial log
            mfsql = "insert into llidc_financial_log (f_o_id,f_o_ip,f_c_acc,f_sales,f_amount,f_otype,f_stype,f_memo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            otype = '1'
            mfval = (oid,ip,cacc,sales,payment,otype,ptype,memo)
            frs = cur.execute(mfsql, mfval)
            #新增提成
            csql = "insert into llidc_commission (com_id,com_oid,com_em,com_cacc,com_ptype,com_opm,com_cm,com_rate,com_memo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            com = 0
            if ptype and ptype.split(",")[0]:
                print "ptype here",i
                ckey = ptype.split(",")[0]
                comid = "llidc"+"-"+getnum(8)+"-com-" + str(int(str(int(time.time()))))+str(random.choice(xrange(500)))
                if ckey in ["r", "s", "t", "u"]:  # "v":"代理机托管","w":"代理机租用"，"k":"加带宽","l":"加防护" 不计算
                    com = com_config[ckey]
                elif ckey in ["x"]:
                    com = payment * com_config[ckey]
                elif ckey in ["v","w"]:#代理提成手工输入
                    com = 0
                cval = (comid, oid, sales, cacc, ptype,payment, com, com_config[ckey], memo)
                comrs = cur.execute(csql, cval)

        if 1000 <= i and i <1500:#续期订单
            print "正在续期订单",i
            soid = "llidc"+"-"+getnum(8)+"-sorder-" + str(int(str(int(time.time()))))+str(random.choice(xrange(500)))
            ssql = "insert into llidc_suborders (s_o_id,s_m_o_id,s_o_details,s_o_pm,s_o_ip,s_o_wsales,s_o_cacc,s_o_memo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            sotype = "f,续期"
            rip = "117.25.154.131"
            wsales = "23,测试"
            cacc = "test001"
            memo = '测试子订单'
            tpm = random.choice(xrange(100))*i
            tid = sid[random.choice(range(len(sid)))]
            sval = (soid,tid,sotype,tpm,rip,wsales,cacc,memo)
            sors = cur.execute(ssql,sval)
            #financial log
            sfsql = "insert into llidc_financial_log (f_o_id,f_o_ip,f_c_acc,f_sales,f_amount,f_otype,f_stype,f_memo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            fltype = financial_log["o"]
            otype = "2"#续期订单归为子订单
            sfval = (tid,rip,cacc,wsales,tpm,otype,sotype,memo)
            frs = cur.execute(sfsql,sfval)
            ptype = "r,普通机托管" if i%2 == 0 else "s,普通机租用" if i % 3 == 0 else "t,高防机托管" if i%7 == 0 else "v,代理机托管" if i%11 == 0 else "x,机柜出租" if i%13 ==0 else "r,普通机托管"
            #commission
            if ptype and ptype.split(",")[0]:
                print "ptype here",i
                ctype = ptype.split(",")[0]#commission type from product type
                ckey = "r"+ctype
                comid = "llidc"+"-"+getnum(8)+"-com-" + str(int(str(int(time.time()))))+str(random.choice(xrange(500)))
                com = 0
                if ckey in ["rr","rs","rt","ru"]:#"v":"代理机托管","w":"代理机租用"，"k":"加带宽","l":"加防护" 不计算
                    com = renew_com_config[ckey]
                elif ckey in ["rx"]:
                    com = tpm*renew_com_config[ckey]
                elif ckey in ["rv","rw"]:#代理提成手工输入
                    com = 0
                csql = "insert into llidc_commission (com_id,com_oid,com_em,com_cacc,com_ptype,com_opm,com_cm,com_rate,com_memo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cval = (comid, tid, wsales, cacc, sotype, tpm, com, renew_com_config[ckey], memo)
                comrs = cur.execute(csql, cval)

        elif i>=1500:#子订单
            print "正在处理子订单",i
            spm = random.choice(xrange(50))*i
            smemo = "子订单"
            stype = "h,加内存" if i%2 == 0 else "i,加硬盘" if i % 3 == 0 else "j,加IP" if i%7 == 0 else "k,加带宽" if i%11 == 0 else "l,加防护" if i%13 ==0 else "h,加内存"
            mid = sid[random.choice(range(len(sid)))]
            cacc = "test001"
            ip = "117.25.154.132"
            osales = "23,测试"
            #add to financial/machine/sub order log
            soid = "llidc"+"-"+getnum(8)+"-sorder-"+str(int(str(int(time.time()))))+str(random.choice(xrange(500)))
            sosql = "insert into llidc_suborders (s_o_id,s_m_o_id,s_o_details,s_o_pm,s_o_ip,s_o_wsales,s_o_cacc,s_o_memo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            soval = (soid,mid,stype,spm,ip,osales,cacc,smemo)
            sors = cur.execute(sosql,soval)
            #add to financial log
            flid = "llidc"+"-"+getnum(8)+"-flog-"+str(int(str(int(time.time()))))+str(random.choice(xrange(500)))
            otype = '2'
            cflsql = "insert into llidc_financial_log(f_o_id,f_o_ip,f_c_acc,f_sales,f_amount,f_otype,f_stype,f_memo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cflval = (soid,ip,cacc,osales,spm,otype,stype,smemo)
            flrs = cur.execute(cflsql,cflval)
            #commission
            sod = stype.split(",")[0]
            comid = "llidc"+"-"+getnum(8)+"-com-" + str(int(str(int(time.time()))))+str(random.choice(xrange(500)))
            print "ptype here",i
            com = 0
            if sod == "k" or sod =="l":
                if sod =="k":#
                    com = spm*com_config["k"]
                elif sod == "l":
                    com = com_config["l"]
                csql = "insert into llidc_commission (com_id,com_oid,com_em,com_cacc,com_ptype,com_opm,com_cm,com_rate,com_memo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cval = (comid,soid,osales,cacc,stype,spm,com,com_config[sod],memo)
                comrs = cur.execute(csql,cval)


finally:
    if cur:
        cnx.commit()
        cur.close()
    if cnx:
        cnx.close()
    # print values
    print "finished all"
