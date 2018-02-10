#!/usr/bin/env python
#coding:utf-8

from __future__ import division
import tornado.web
from pyquery import PyQuery as pq
import os,re,sys,math,random,json,time,datetime,calendar,base64,re,traceback
from template.wmodules import *
from app.webCaptcha import webCaptcha
from tornado.escape import json_decode,json_encode
from tornado import gen
from config.settings import websettings as wst
import hashlib
from datetime import datetime as dt
from config.settings import com_config,renew_com_config,financial_log,msg_config,em_sales,order_renew_type
from tornado.httpclient import AsyncHTTPClient
from tornado.httputil import url_concat
from collections import OrderedDict
from io import BytesIO as StringIO #py2.7 will confuse about StringIO
from pyexcel_xlsx import save_data

__metaclass__ = type

class baseHandler(tornado.web.RequestHandler):
    def __init__(self,application,*args,**kwds):
        tornado.web.RequestHandler.__init__(self,application,*args,**kwds)
        self.thisyear = dt.now().year
        self.ctype = ""#user type
        self.uname = ""#user name
        #print self.get_secure_cookie("_n")
        x_real_ip = self.request.headers.get("X-Real-IP")
        self.ua = self.request.headers.get("User-Agent")
        self.path = self.request.uri
        self.remote_ip = x_real_ip or self.request.remote_ip  # when use nginx we get x_real_ip or we just get remote_ip
        if self.get_secure_cookie("_ac") and not self.ctype:
            if self.request.uri.startswith("/admin"):
                sql = "SELECT * FROM llidc_employees"
                where = "binary u_acc = '%s'" % self.get_secure_cookie("_ac")
                em = self.db.where(where).getone(sql)
                self.ctype = em[5]
                self.uname = em[2]
                self.eid = em[0]
            #elif self.request.uri.startswith("/client"):

    def get_current_user(self):
        """{current_user} in template,request:self.current_user"""
        return self.get_secure_cookie("_n")

    @classmethod
    def getnum(cls, n=5):#get n random num
        a = []
        cset = [chr(i) for i in range(1, 256) if chr(i).isdigit()]  # alphabet or number
        for i in range(1, n + 1):
            a.append(random.choice(cset))
        return "".join(a)


    def write_error(self,status_code,**kwargs):
        if wst['debug']:
            self.set_header('Content-Type', 'text/plain')
            for line in traceback.format_exception(*kwargs["exc_info"]):
                self.write(line)
            self.finish()
        elif status_code:
            return self.render("error.html",active="index")

    @property
    def db(self):
        return self.application.db

class mainHandler(baseHandler):
    def get(self):
        #self.send_error(404)
        #time.sleep(random.choice(range(3,6)))
        active ="index"
        sql = "select * from llidc_news"
        newscond = "n_type = 1"
        noticecond = "n_type = 2"
        news = self.db.where(newscond).orderby("n_datetime","desc").limit(4).getmany(sql)
        #news = self.db.orderby("n_datetime", "desc").limit(4).getmany(sql)
        notices = self.db.where(noticecond).orderby("n_datetime","desc").limit(4).getmany(sql)
        return self.render("index.html",active=active,news = news,notices = notices)
    def post(self):
        pass

class rentHandler(baseHandler):

    def get(self):
        active ="rent"
        return self.render("rent.html",active=active)

    def post(self):
        pass

class hostHandler(baseHandler):

    def get(self):
        active ="host"
        return self.render("host.html",active=active)

    def post(self):
        pass

class contactHandler(baseHandler):

    def get(self):
        active ="contact"
        return self.render("contact.html",active=active)

    def post(self):
        pass

class solutionHandler(baseHandler):

    def get(self):
        active ="slt"
        return self.render("solution.html",active=active)

    def post(self):
        pass

class vistHandler(baseHandler):
    def get(self):
        active ="visit"
        return self.render("visit.html",active=active)

    def post(self):
        pass

class newsHandler(baseHandler):
    def get(self,id):
        active ="index"
        cond = "n_id = '%s'"%id
        sql = "select * from llidc_news"
        news = self.db.where(cond).getone(sql)
        return self.render("news.html",active=active,news = news)
    def post(self):
        pass

class activitiesHandler(baseHandler):
    def get(self):
        active ="solution"
        return self.render("activities.html",active=active)
    def post(self):
        pass

class asServiceHandler(baseHandler):
    def get(self):
        active = ""
        return self.render("as-service.html", active=active)
    def post(self):
        self.send_error(403)

class serviceContractHandler(baseHandler):

    def get(self):
        active = ""
        return self.render("service-contract.html", active=active)

    def post(self):
        self.send_error(403)

class adminLoginHandler(baseHandler):
    def get(self):
        if self.get_secure_cookie("_n"):
            active = "index"
            return self.redirect("/admin/overview/")
        imgc = webCaptcha()
        imglist = imgc.saveImg()
        thiscc = imglist[1]  # 当前的验证码
        self.set_secure_cookie("cc",thiscc,expires_days=1)
        return self.render("admin/admin_login.html",acc=imglist[0])

    def post(self):
        uacc = self.get_argument("uacc")
        ampwd = self.get_argument("upwd")
        md5 = hashlib.md5()
        md5.update(ampwd + "llidc")
        ampwded = md5.hexdigest()
        sql = "SELECT * FROM llidc_employees"
        where = "BINARY u_acc = '%s'" % uacc#case sensitive
        em = self.db.where(where).getone(sql)
        active = "index"
        if ampwded == em[3]:
            self.set_secure_cookie("_n",em[2])
            self.set_secure_cookie("_ac", em[1])
            next = self.get_argument("next", "")
            if next:
                return self.redirect(next)  # rediret to the previous url
            return self.redirect("/admin/redirect/")
        else:
            self.redirect("/")


#generate captcha
class captchaHandler(baseHandler):
    def get(self):
        """get current timestamp,if abuse then forbid,one ip"""
        tstamp = self.get_argument("tstamp","")
        lstamp = self.get_secure_cookie("ts")#获取上次生成验证的时间
        if not lstamp:
            self.set_secure_cookie("ts",tstamp,2)
            imgc = webCaptcha()
            imglist = imgc.saveImg()
            thiscc = imglist[1]  # 当前验证码
            self.set_secure_cookie("cc", thiscc, 1)
            imgjson = json.dumps({"imgsrc": imglist[0]})
            return self.write(imgjson)
        else:
            self.set_secure_cookie("ts",lstamp+","+tstamp)
            td = [int(i) for i in (lstamp+","+tstamp).split(",")]
        if len(td) >5 and len(td)%2 ==0:
            diff = reduce(lambda x,y:y-x,td)
            if diff<3000:
                self.set_secure_cookie("ts",tstamp,2)
                imgc = webCaptcha()
                imglist = imgc.saveImg()
                thiscc = imglist[1]  # 当前验证码
                self.set_secure_cookie("cc", thiscc, 1)
                #imgjson = json.dumps({"imgsrc": imglist[0],"cre":1})
                return self.write(json.dumps({"tscre":{"imgsrc": imglist[0],"cre":1}}))
            else:
                self.set_secure_cookie("ts", tstamp, 2)
                imgc = webCaptcha()
                imglist = imgc.saveImg()
                thiscc = imglist[1]  # 当前验证码
                self.set_secure_cookie("cc", thiscc, 1)
                imgjson = json.dumps({"imgsrc": imglist[0]})
                return self.write(imgjson)
        else:
            imgc = webCaptcha()
            imglist = imgc.saveImg()
            thiscc = imglist[1]  # 当前验证码
            self.set_secure_cookie("cc", thiscc, 1)
            imgjson = json.dumps({"imgsrc": imglist[0]})
            return self.write(imgjson)


#check captcha
class checkCaptchaHandler(baseHandler):
    def get(self):
        cc = self.get_query_argument("cc", "").upper()
        if cc:
            # 验证用户输入的验证码
            ckcc = self.get_secure_cookie("cc").upper()
            if cc != ckcc:
                ccerr = {"cre": 1}
                return self.write(json.dumps(ccerr))
            else:
                cccr = {"cre": 0}
                return self.write(json.dumps(cccr))
        else:
            self.send_error(403)

    def post(self):
        pass

class adminOverviewHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        active = "index"
        return self.render("admin/admin_overview.html",active=active,ctype=self.ctype,eid=self.eid)

    def post(self):
        self.send_error(403)

#log out
class quitHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.clear_cookie("_n")
        self.redirect("/")

class adminAllMahcinesHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        offset = int(self.get_argument("offset", "1")) - 1
        mroom = self.get_argument("mroom","")#machine location
        mtype = self.get_argument("mtype","") #mtype
        mstatus = self.get_argument("mstatus","")  # machine status
        cnum = self.get_argument("cnum", "")  # caninet num
        ips = self.get_argument("ips","")#ips num
        sql = "select * from llidc_machines"
        csql = "select count(*) from llidc_machines"
        field = "m_reg_time"
        num = 13
        condition = "m_type = '%s'" % mtype
        #required conditions
        if mroom:
            condition += " and m_idc_location regexp '%s'" % mroom
        if cnum:
            condition += " and m_cabinet_num = '%s'" % cnum
        if ips:
            condition += " and m_ip regexp '%s'" % ips
        #check which type of kwds and necessary requirements.
        if mtype == "0":
            anum = self.get_argument("anum", "")  # asset num
            onum = self.get_argument("onum", "")  # other machine's num
            if anum:
                condition += " and m_num = '%s'"%anum
            if onum:
                condition += " and m_num_wy = '%s'"%onum
        elif mtype =="1":
            bm_mnum = self.get_argument("bm_mnum", "")  # bm_num
            lip = self.get_argument("lip", "")  # local ip
            if bm_mnum:
                condition += " and m_bm_mnum = '%s'"%bm_mnum
            elif lip:
                condition += " and m_bm_ip = '%s'"%lip
        if mstatus:
            condition += " and m_status regexp '%s'" %mstatus
        count = self.db.where(condition).getsum(csql)  # total num of machines
        # print count
        if count % num == 0:
            pages = count // num
        else:
            pages = count // num + 1
        ms = self.db.where(condition).orderby(field, "desc").limit((offset) * 13, num).getmany(sql)
        if mtype == "0":
            return self.render("admin/admin_machines.html", ms=ms, count=count, active="machines", pages=pages,offset=offset+1,ctype = self.ctype,eid=self.eid,mtype = mtype,mroom = mroom,cnum = cnum,anum = anum,onum = onum,mstatus=mstatus,ips=ips)
        elif mtype == "1":#blade machine
            return self.render("admin/admin_machines_bm.html", ms=ms, count=count, active="machines", pages=pages,offset=offset + 1, ctype=self.ctype, eid = self.eid,mtype=mtype,mroom = mroom,cnum = cnum,bm_mnum = bm_mnum,lip = lip,mstatus=mstatus,ips=ips)


class adminRedirectHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("admin/admin_redirect.html",active = "index",ctype = self.ctype,eid=self.eid)

class adminMachinesHandler(baseHandler):
    def get(self):
        self.send_error(403)
    @tornado.web.authenticated
    def post(self):
        mtype = self.get_argument("mtype","")#machine's type
        ip = self.get_argument("ips","")#machine's ip
        loca = self.get_argument("loca","")#location of the machine
        cabi = self.get_argument("c_num","")#cabinet num
        num = self.get_argument("m_num","")#machine num,unique
        wy_num = self.get_argument("wy_m_num","")#same as above,unique
        bw = self.get_argument("bw","")#bandwidth
        status = self.get_argument("status","")#machine status
        config = self.get_argument("config","")#machine's configuration
        memo = self.get_argument("memo","")#machine's memo
        if mtype == "0":
            sql = "insert into llidc_machines (m_ip,m_idc_location,m_cabinet_num,m_num,m_num_wy,m_bandwidth,m_status,m_config,m_memo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (ip,loca,cabi,num,wy_num,bw,status,config,memo)
        elif mtype == "1":
            bm_mnum = self.get_argument("bm_mnum", "")  # bm machine;s mother number
            bm_num = self.get_argument("bm_num", "")  # bm machine's number
            bm_ip = self.get_argument("bm_ip", "")  # bm_machine's ip
            sql = "insert into llidc_machines (m_ip,m_idc_location,m_cabinet_num,m_num,m_num_wy,m_bandwidth,m_status,m_config,m_memo,m_type,m_bm_mnum,m_bm_num,m_bm_ip) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (ip, loca, cabi, num, wy_num, bw, status, config, memo,mtype)
        result = self.db.insertone(sql,values)
        if result:
            self.finish(json_encode({"rs":"1024"}))#successfully added the machine
        else:
            self.finish(json_encode({"rs": "1025"}))  # fail to  add the machine


class adminMachineCheckHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        """ if multi ips exist"""
        ip = self.get_argument("ip","")
        multi = self.get_argument("multi","")
        csql = "select m_ip,m_num from llidc_machines"
        asnum = self.get_argument("asnum","")
        if not asnum:
            if multi == "1":
                mcond = "m_ip regexp '%s$'" % ip
                ifmex = self.db.where(mcond).checkIfExist(csql)
                if not ifmex:
                    #multi ips check each one
                    ips = ip.split(",")
                    ifoex = False
                    exip = ''
                    for i in ips:
                        ccond = "m_ip regexp '%s'" %i
                        mrs = self.db.where(ccond).getmany(csql)#if this ip doesn't exist
                        if len(mrs):
                            for j in mrs:
                                if "," in j[0]:
                                    if i in j[0].split(","):
                                        exip = i
                                        ifoex = True
                                        break
                                elif j[0] == i:
                                    exip = i
                                    ifoex = True
                                    break
                    if ifoex:
                        return self.finish(json_encode({"rs": "1046","exip":exip}))#ip has been used
                    else:
                        return self.finish(json_encode({"rs": "1047"}))#available
                elif ifmex:
                    #if multi ip match equally
                    return self.finish(json_encode({"rs": "1046","exip":ip}))
            elif multi == "0":
                scond = "m_ip regexp '%s'" % ip
                srs = self.db.where(scond).getmany(csql)
                ifex = False
                exip = ''
                if len(srs):
                    for i in srs:
                        if "," in i[0]:
                            if ip in i[0].split(","):
                                ifex = True
                                exip = ip
                                break
                        else:
                            if i[0] == ip:
                                ifex = True
                                exip = ip
                                break
                if ifex:
                    return self.finish(json_encode({"rs": "1046","exip":exip}))
                else:
                    return self.finish(json_encode({"rs": "1047"}))# if this ip doesn't exist

        else:
            #check if there is assert num
            ascond = "m_num regexp '%s$'"%asnum
            asrs = self.db.where(ascond).checkIfExist(csql)
            if asrs:
                return self.finish(json_encode({"rs": "1048"}))  #not available
            else:
                return self.finish(json_encode({"rs": "1049"}))  # assert num available

class adminOrdersHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        """join machines and orders table"""
        offset = int(self.get_argument("offset", "1")) - 1
        wsales = self.get_argument("wsales",str(self.eid)+','+self.uname)#which sales'order
        expire = self.get_argument("expire","")
        obexpire = self.get_argument("obexpire","")#order by expire time
        obamount = self.get_argument("obamount","")#order by order payment amount
        obstart  = self.get_argument("obstart","")#order by start time
        stype = self.get_argument("stype","")#service type
        ips = self.get_argument("ips", "")  # unicode to utf8
        u_acc = self.get_argument("u_acc","")#client account
        asnum = self.get_argument("asnum","")#asset num
        ifad = self.get_argument("ifad","")#if order is audited
        sql = "select * from llidc_orders o join llidc_clients c on o.o_c_acc = c.c_acc join llidc_machines m on o.o_ip = m.m_ip"
        csql = "select count(*) from llidc_orders o join llidc_clients c on o.o_c_acc = c.c_acc join llidc_machines m on o.o_ip = m.m_ip"
        condition = "1"
        field = "o.o_id"
        sum = 0
        if obexpire:
            field1 = "o.o_expire_datetime"
        if obamount:
            field2 = "o.o_payment"
        if obstart:
            field3 = 'o.o_start_datetime'
        num = 20
        if ips:
            condition += " and o.o_ip regexp '%s'"%ips
        if u_acc:
            condition += " and binary o.o_c_acc = '%s'"%u_acc
        if wsales:
            condition += " and o.o_sales regexp '%s'"%wsales.split(',')[0]
        if asnum:
            condition += " and m.m_num regexp '%s'"%asnum
        if stype:
            condition += " and m.m_status regexp '%s'"%stype
        if expire =="1":
            condition += " and o.o_expire_datetime < '%s'"%dt.strftime(datetime.datetime.now(),"%Y-%m-%d")
        elif expire =="2":
            condition += " and o.o_expire_datetime between '%s' and '%s'"%(dt.strftime(dt.now(),"%Y-%m-%d"),dt.strftime(dt.now()+datetime.timedelta(3),"%Y-%m-%d"))
        elif expire =="3":
            condition += " and o.o_expire_datetime between '%s' and '%s'" % (dt.strftime(dt.now(),"%Y-%m-%d"),dt.strftime(dt.now() + datetime.timedelta(7), "%Y-%m-%d"))
        # print count
        if self.ctype in [3,4,5]:  # admin check all orders details
            if wsales:
                ssql = "select sum(f_amount) from llidc_financial_log"
                scond = "f_sales regexp '%s'" % self.eid
                sum = self.db.where(scond).getsum(ssql)
        else:
            sum = 0#admins except employees can check others orders details.
        count = self.db.where(condition).getsum(csql)  # total num of orders
        if count % num == 0:
            pages = count // num
        else:
            pages = count // num + 1
        #ordering
        if obexpire:
            orders = self.db.where(condition).orderby(field1, obexpire).limit((offset) * 13, num).getmany(sql)
            return self.render("admin/admin_orders.html", orders=orders, count=count, active="orders", pages=pages,offset=offset + 1,
                               ctype=self.ctype, stype=stype, u_acc=u_acc, ips=ips, expire=expire,obexpire=obexpire, obamount="",
                               asnum=asnum, obstart="",wsales=wsales,sum=sum,eid=self.eid,ifad=ifad)

        elif obamount:
            orders = self.db.where(condition).orderby(field2, obamount).limit((offset) * 13, num).getmany(sql)
            return self.render("admin/admin_orders.html", orders=orders, count=count, active="orders", pages=pages,
                               offset=offset + 1, ctype=self.ctype, eid=self.eid,stype=stype, u_acc=u_acc, ips=ips, expire=expire,
                               obexpire="", obamount=obamount, asnum=asnum, obstart="",wsales=wsales,sum=sum,ifad=ifad)
        elif obstart:
            orders = self.db.where(condition).orderby(field3, obstart).limit((offset) * 13, num).getmany(sql)
            return self.render("admin/admin_orders.html", orders=orders, count=count, active="orders", pages=pages,
                               offset=offset + 1, ctype=self.ctype, stype=stype,eid=self.eid, u_acc=u_acc, ips=ips, expire=expire,
                               obexpire="", obamount="", asnum=asnum, obstart=obstart,wsales=wsales,sum=sum,ifad=ifad)
        else:
            orders = self.db.where(condition).orderby(field,"desc").limit((offset) * 13, num).getmany(sql)
            return self.render("admin/admin_orders.html",orders=orders,count=count,active="orders",pages=pages,offset=offset + 1, ctype=self.ctype,stype = stype,eid=self.eid,
                               u_acc = u_acc,ips = ips,expire = expire,obexpire = "",obamount = "",asnum = asnum,obstart = "",wsales=wsales,sum=sum,ifad=ifad)

    @tornado.web.authenticated
    def post(self):
        #auditor will not put here
        ip = self.get_argument("ips","")#machine's ip
        cacc = self.get_argument("cacc","")#client's id
        payment = int(self.get_argument("pm"))#order payment amount
        sd = self.get_argument("sdt","")#the time order starts from
        msl = int(self.get_argument("msl",""))#the month service lasts
        stype = self.get_argument("stype","")#order status
        ptype = self.get_argument("ptype","")#product type
        sales = self.get_argument("sales","")#to whom the order belongs to
        memo = self.get_argument("memo","")#memo of the order
        cmonth = datetime.datetime.strptime(sd,"%Y/%m/%d").month
        cyear = datetime.datetime.strptime(sd,"%Y/%m/%d").year
        pms = self.get_argument("pmsource")#payment source
        mloca = self.get_argument("idcloca","")#idc location

        if cmonth+msl>12:
            # calculate this year
            mnext = cmonth+msl-12
            nyear = cyear+1
            exdays = sum([calendar.monthrange(cyear, i)[1] for i in range(cmonth, 13)])
            # cal next year
            exdays += sum([calendar.monthrange(nyear, j)[1] for j in range(1,mnext+1)])-1
        else:
            # calculate this year
            exdays = sum([calendar.monthrange(cyear, i)[1] for i in range(cmonth, cmonth + msl+1)])-1  # max days of current month plus max days of the comming
        expire = dt.strftime(dt.strptime(sd,'%Y/%m/%d') + datetime.timedelta(days=exdays), '%Y/%m/%d')
        sql = "insert into llidc_orders (o_ip,o_c_acc,o_payment,o_start_datetime,o_expire_datetime,o_m_stype,o_ptype,o_sales,o_memo,o_pm_source) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (ip,cacc,payment,sd,expire,stype,ptype,sales,memo,pms)
        lastid = self.db.insertone(sql,values)
        if lastid:
            #modify machine's status according to service type
            sql = "update llidc_machines set m_status = '%s',m_sales = '%s'"%(ptype,sales)
            condition = "m_ip = '%s' and m_status regexp '%s'" % (ip,"a")
            udrs = self.db.where(condition).updateone(sql)
            if not udrs:
                self.finish(json_encode({"rs": "1058"}))  # machine is being used
            #write to fiancial log
            otype = "1"
            fsql = "insert into llidc_financial_log (f_o_id,f_o_ip,f_c_acc,f_sales,f_amount,f_stype,f_otype,f_memo,f_idc_loca,f_pm_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            fval = (lastid,ip,cacc,sales,payment,ptype,otype,memo,mloca,pms)
            frs = self.db.insertone(fsql, fval)
            #calculate commission
            csql = "insert into llidc_commission (com_oid,com_em,com_cacc,com_ptype,com_opm,com_cm,com_rate,com_memo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            com = 0
            if ptype and ptype.split(",")[0]:
                ckey = ptype.split(",")[0]
                if ckey in ["r", "s", "t", "u"]:  # "v":"代理机托管","w":"代理机租用"，"k":"加带宽","l":"加防护" 不计算
                    com = com_config[ckey]
                elif ckey in ["x"]:
                    com = payment * com_config[ckey]
                elif ckey in ["v","w"]:#代理提成手工输入
                    com = 0
                cval = ( lastid, sales, cacc, ptype,payment, com, com_config[ckey], memo)
                comrs = self.db.insertone(csql, cval)
                if frs and comrs:
                    self.finish(json_encode({"rs": "1026"}))  # successfully added the order
        else:
            self.finish(json_encode({"rs": "1027"}))  # fail to  add the order


class adminOrderExportHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        """join machines and orders table"""
        offset = int(self.get_argument("offset", "1")) - 1
        wsales = self.get_argument("wsales", str(self.eid) + ',' + self.uname)  # which sales'order
        expire = self.get_argument("expire", "")
        obexpire = self.get_argument("obexpire", "")  # order by expire time
        obamount = self.get_argument("obamount", "")  # order by order payment amount
        obstart = self.get_argument("obstart", "")  # order by start time
        stype = self.get_argument("stype", "")  # service type
        ips = self.get_argument("ips", "")  # unicode to utf8
        u_acc = self.get_argument("u_acc", "")  # client account
        asnum = self.get_argument("asnum", "")  # asset num
        sql = "select * from llidc_orders o join llidc_clients c on o.o_c_acc = c.c_acc join llidc_machines m on o.o_ip = m.m_ip"
        condition = "1"
        field = "o.o_id"
        if obexpire:
            field1 = "o.o_expire_datetime"
        if obamount:
            field2 = "o.o_payment"
        if obstart:
            field3 = 'o.o_start_datetime'
        if ips:
            condition += " and o.o_ip regexp '%s'" % ips
        if u_acc:
            condition += " and binary o.o_c_acc = '%s'" % u_acc
        if wsales:
            condition += " and o.o_sales regexp '%s'" % wsales.split(',')[0]
        if asnum:
            condition += " and m.m_num regexp '%s'" % asnum
        if stype:
            condition += " and m.m_status regexp '%s'" % stype
        if expire == "1":
            condition += " and o.o_expire_datetime < '%s'" % dt.strftime(datetime.datetime.now(), "%Y-%m-%d")
        elif expire == "2":
            condition += " and o.o_expire_datetime between '%s' and '%s'" % (
            dt.strftime(dt.now(), "%Y-%m-%d"), dt.strftime(dt.now() + datetime.timedelta(3), "%Y-%m-%d"))
        elif expire == "3":
            condition += " and o.o_expire_datetime between '%s' and '%s'" % (
            dt.strftime(dt.now(), "%Y-%m-%d"), dt.strftime(dt.now() + datetime.timedelta(7), "%Y-%m-%d"))
        # print count
        if self.ctype in [1, 2, 3, 4]:
            condition += " and o_auditors is not null"
        filename = wsales.split(',')[1]+"-"+dt.strftime(dt.now() + datetime.timedelta(3), "%Y-%m-%d %H:%M:%S")+".xlsx"
        #print filename
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename="' + filename+'"')
        orders = self.db.where(condition).orderby(field, "desc").getmany(sql)
        orders = map(lambda y:map(lambda x: dt.strftime(x, '%Y/%m/%d') if isinstance(x,(datetime.datetime, datetime.date)) else x,y),orders) if orders else ""#stringfy datetime type
        orders = map(lambda y:map(lambda x: str(x) if isinstance(x,long) else x, y),orders) if orders else ""#remove null
        orders = map(lambda y: map(lambda x: x.decode('utf-8') if isinstance(x,str) else x, y),orders)#to unicode
        orders = map(lambda y: map(lambda x: x if x else "", y),orders)
        data = OrderedDict()
        data.update({"Sheet 1": [list(i) for i in orders]})
        f = StringIO()
        save_data(f,data)
        f.seek(0)
        while True:
            data = f.readline()
            if not data:
                break
            self.write(data)
        self.finish()

class adminOrdersModifyHandler(baseHandler):
    @tornado.web.authenticated
    def get(self,oid):
        sql = "select * from llidc_orders o join llidc_clients c on o.o_c_acc = c.c_acc join llidc_machines m on o.o_ip = m.m_ip"#join tables
        condition = "o.o_id = '%s'"%oid
        order = self.db.where(condition).getone(sql)
        order = map(lambda x: dt.strftime(x, '%Y/%m/%d') if isinstance(x,(datetime.datetime, datetime.date)) else x,order)#stringfy datetime type
        order = map(lambda x: x if x else "", order)#remove null
        #select sub order
        ssql = "select * from llidc_suborders"
        scond = "s_m_o_id = '%s'"%oid
        sorder = self.db.where(scond).getmany(ssql)
        sorder = map(lambda y:map(lambda x: dt.strftime(x, '%Y/%m/%d') if isinstance(x,(datetime.datetime, datetime.date)) else x,y),sorder) if sorder else ""#stringfy datetime type
        sorder = map(lambda y:map(lambda x: x if x else "", y),sorder) if sorder else ""#remove null
        return self.finish(json_encode({"order":order,"suborder":sorder}))

    @tornado.web.authenticated
    def post(self,oid):
        med = self.get_argument("med")
        mmemo = self.get_argument("mmemo","")
        msql = "update llidc_orders set o_expire_datetime = '%s',o_memo = '%s'"%(med,mmemo)
        mcond = "o_id = '%s'"%oid
        mrs = self.db.where(mcond).updateone(msql)
        if mrs:
            return self.finish(json_encode({"rs":"1042"}))#successfully modify the order
        else:
            return self.finish(json_encode({"rs":"1043"}))

class removeMachineHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.send_error(403)

    @tornado.web.authenticated
    def post(self,tid):
        #print tid
        sql = "delete from llidc_machines"
        condition = "m_id = '%s'"%tid
        result = self.db.where(condition).remove(sql)
        if result:
            self.finish(json_encode({"rs":"1028"}))
        else:
            self.finish(json_encode({"rs":"1029"}))

class adminOrderRenewHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.send_error("403")

    @tornado.web.authenticated
    def post(self):
        tid = self.get_argument("tid","")#order id
        pm = int(self.get_argument("pm"))#payment amount
        renew = int(self.get_argument("renew"))#date renew to
        memo = self.get_argument("memo","")#renew memo
        eed = dt.strptime(self.get_argument("exd",""),'%Y/%m/%d')#estimated expire date
        tpm = int(self.get_argument("tpm"))#payment client made this time
        ptype = self.get_argument("ptype")#product type
        wsales = self.get_argument("wsales","")
        rip = self.get_argument("rip","")
        mloca = self.get_argument("idcloca")#idc location
        pmtype = self.get_argument("pmsource","")#payment type
        cmonth = eed.month
        cyear = eed.year
        if cmonth+renew>12:
            # calculate this year
            mnext = cmonth+renew-12
            nyear = cyear+1
            exdays = sum([calendar.monthrange(cyear, i)[1] for i in range(cmonth, 13)])
            # cal next year
            exdays += sum([calendar.monthrange(nyear, j)[1] for j in range(1,mnext+1)])-1
        else:
            # calculate this year
            exdays = sum([calendar.monthrange(cyear, i)[1] for i in range(cmonth, cmonth + renew+1)])-1  # max days of current month plus max days of the comming
        expire = dt.strftime(eed+datetime.timedelta(days=exdays),'%Y/%m/%d')
        cacc = self.get_argument("cacc","")
        #expire = eed+datetime.timedelta(days=exdays)
        sql = "update llidc_orders set o_expire_datetime = '%s',o_memo = '%s'"%(expire,memo)#while order amount is accumulated
        condition = "o_id = '%s'"%tid
        rs = self.db.where(condition).updateone(sql)
        #write to sub order record
        ssql = "insert into llidc_suborders (s_m_o_id,s_o_details,s_o_pm,s_o_ip,s_o_wsales,s_o_cacc,s_o_memo,s_pm_type) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        sokey = "r"+ ptype.split(",")[0]
        #print type(order_renew_type[sokey])
        sotype = sokey+u","+order_renew_type[sokey].decode('utf-8')
        sval = (tid,sotype,tpm,rip,wsales,cacc,memo,pmtype)
        sors = self.db.insertone(ssql,sval)
        if rs and sors:
            #write to financial log,
            pm_date = ""
            fsql = "insert into llidc_financial_log (f_o_id,f_o_ip,f_c_acc,f_sales,f_amount,f_otype,f_stype,f_memo,f_idc_loca,f_pm_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            otype = "2"#续期订单归为子订单
            fval = (sors,rip,cacc,wsales,tpm,otype,sotype,memo,mloca,pmtype)#add suborder id to financial log
            frs = self.db.insertone(fsql,fval)
            #commission
            if ptype and ptype.split(",")[0]:
                ctype = ptype.split(",")[0]#commission type from product type
                ckey = "r"+ctype
                com = 0
                if ckey in ["rr","rs","rt","ru"]:#"v":"代理机托管","w":"代理机租用"，"k":"加带宽","l":"加防护" 不计算
                    com = renew_com_config[ckey]
                elif ckey in ["rx"]:
                    com = tpm*renew_com_config[ckey]
                elif ckey in ["rv","rw"]:#代理提成手工输入
                    com = 0
                csql = "insert into llidc_commission (com_oid,com_em,com_cacc,com_ptype,com_opm,com_cm,com_rate,com_memo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                cval = ( sors, wsales, cacc, sotype, tpm, com, renew_com_config[ckey], memo)#add suborder id to commission log
                comrs = self.db.insertone(csql, cval)
            if frs and comrs:
                return self.finish(json_encode({"rs":"1030"}))#order renewed successfully
        else:
            return self.finish(json_encode({"rs": "1031"}))#fail to renew order

class adminOrderAuditHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.send_error(403)

    @tornado.web.authenticated
    def post(self):
        oid = self.get_argument("oid")
        auditor = self.get_argument("auditor")
        sql = "update llidc_orders set o_auditors = '%s',o_audit_time = '%s'"%(auditor,dt.strftime(dt.now(),"%Y-%m-%d %H:%M:%S"))
        condition = "o_id = '%s'"%oid
        rs = self.db.where(condition).updateone(sql)
        if rs:
            return self.finish(json_encode({"rs":1032}))
        else:
            return self.finish(json_encode({"rs":1033}))

class adminPublishHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("admin/admin_publish.html",ctype = self.ctype,eid=self.eid,active = "publish")

    @tornado.web.authenticated
    def post(self):
        nid = "llidc-news-"+ baseHandler.getnum(6)+str(int(str(int(time.time())*6)))
        title = self.get_argument("title","")#news title
        ntype = self.get_argument("ntype","")#news type
        content = self.get_argument("contents","")#news content
        html = pq(content)
        imgs = html.find("img")#find all imgs
        testdir = wst["tndir"]+nid+"\\"
        pdir = wst["ndir"]+nid+"\\"
        if not os.path.isdir(pdir):
            os.mkdir(pdir)
        if len(imgs):
            for i in range(len(imgs)):
                if imgs.eq(i).attr("src").startswith("data:image"):#only process base64 img string
                    b64str = imgs.eq(i).attr("src")
                    imgstr = b64str.split("base64,")[1]
                    pat = re.compile("image\/(.*);")
                    type = pat.search(b64str).group(1)
                    name = "llidc-news-"+str(int(str(int(time.time())))*random.choice(range(1,10)))+"."+type
                    with open(pdir+name,"wb") as f:
                        f.write(base64.b64decode(imgstr))
                        #new img src
                        imgs.eq(i).attr("src","/static/img/news/"+nid+"/"+name)
        sql = "insert into llidc_news (n_id,n_title,n_content,n_type) values(%s,%s,%s,%s)"
        values = (nid,title,html.html(),ntype)
        rs = self.db.insertone(sql,values)
        if rs:
            return self.render("admin/admin_finish_publish.html",ctype=self.ctype,eid=self.eid,nid = nid,active="publish")
        else:
            self.send_error(404)

class adminMachineModifyHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.send_error(403)

    @tornado.web.authenticated
    def post(self):
        tid = self.get_argument("tid","")#machine id
        #loca = self.get_argument("loca", "")  # location of the machine
        cnum = self.get_argument("cnum","")#caninet num
        ip = self.get_argument("ips", "")  # machine's ip
        config = self.get_argument("config", "")  # machine's configuration
        anum = self.get_argument("anum", "")  # asset's num
        onum = self.get_argument("onum", "")  # related num
        bw = self.get_argument("bw", "")  # bandwidth
        wsales = self.get_argument("wsales", "")  # machine is owned by which sales
        status = self.get_argument("status", "")  # machine status
        memo = self.get_argument("memo", "")  # machine's memo
        values = (ip,cnum,anum,onum,bw,wsales,status,config,memo)
        sql = "update llidc_machines set m_ip = '%s',m_cabinet_num = '%s',m_num = '%s',m_num_wy = '%s',m_bandwidth = '%s',m_sales = '%s',m_status = '%s',m_config = '%s',m_memo ='%s'"%values
        condition = "m_id = '%s'"%tid
        rs = self.db.where(condition).updateone(sql)
        if rs:
            return self.finish(json_encode({"rs":1032}))#successfully udpated
        else:
            return self.finish(json_encode({"rs":1033}))#fail to update

class adminOrderCheckHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        """ if multi ips exist"""
        ip = self.get_argument("ip")
        multi = self.get_argument("multi")
        csql = "select * from llidc_machines"
        scond = "m_ip = '%s' and m_status regexp 'a'" %ip
        ifex = self.db.where(scond).getone(csql)#check if
        if multi == "1" and not ifex:
            ips = ip.split(",")
            acr = True
            for i in ips:
                ccond = "m_ip = '%s' and m_status regexp 'a'"%i#only when machine is vacant
                ifsubex = self.db.where(ccond).getone(csql)#if this ip doesn't exist
                if not ifsubex:
                    acr = False if acr else False
                    break
            if acr:
                return self.finish(json_encode({"rs":"1044","loca":ifsubex[2]}))#available
            else:
                return self.finish(json_encode({"rs":"1045"}))
        if ifex:
            return self.finish(json_encode({"rs": "1044","loca":ifex[2]}))
        else:
            return self.finish(json_encode({"rs": "1045"}))

    @tornado.web.authenticated
    def post(self):
        pass

class adminOrderReleaseHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.send_error(403)

    @tornado.web.authenticated
    def post(self):
        oid = self.get_argument("oid","")
        ip = self.get_argument("ip","")
        orstatus = "e,失效"
        mrstatus = "f,回收"
        orsql = "update llidc_orders set o_m_stype = '%s'"%orstatus
        ocond = "o_id = '%s'"%oid
        ors = self.db.where(ocond).updateone(orsql)
        mrsql = "update llidc_machines set m_status = '%s'"%mrstatus
        mcond = "m_ip = '%s'"%ip
        mrs = self.db.where(mcond).updateone(mrsql)
        if ors and mrs:
            return self.finish(json_encode({"rs":1034}))#successfully release the machine,and set the order expired
        else:
            return self.finish(json_encode({"rs":1035}))

class adminOrderRemoveHandler(baseHandler):
    @tornado.web.authenticated
    def post(self,oid):
        csql = "select o_expire_datetime from llidc_orders"
        cond = "o_id = '%s'"%oid
        expire = self.db.where(cond).getone(csql)[0]
        if dt.strftime(dt.now(),"%Y/%m%d") > dt.strftime(expire,"%Y/%m%d"):
            rmsql = "delete from llidc_orders"
            drs = self.db.where(cond).remove(rmsql)
            if drs:
                return self.finish(json_encode({"rs":"1052"}))#successfully remove the order
            else:
                return self.finish(json_encode({"rs": "1053"}))#fail to remove
        else:
            return self.finish(json_encode({"rs": "1054"})) #expire is before now



    @tornado.web.authenticated
    def get(self):
        pass

class adminMachineReleaseHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.send_error(403)

    @tornado.web.authenticated
    def post(self):
        mid = self.get_argument("mid","")
        mst = "a,空闲"
        mcond = "m_id = '%s'"%mid
        msql = "update llidc_machines set m_status = '%s'"%mst
        mrs = self.db.where(mcond).updateone(msql)
        #add record to machine log
        if mrs:
            return self.finish(json_encode({"rs":"1036"}))#successfully release the machine
        else:
            return self.finish(json_encode({"rs":"1037"}))

class adminSuborderHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.send_error(403)

    @tornado.web.authenticated
    def post(self):
        """only add bandwidth,add defence will bring commission"""
        spm = int(self.get_argument("spm",""))
        smemo = self.get_argument("smemo").upper()
        stype = self.get_argument("ostype")
        mid = self.get_argument("mid")
        cacc = self.get_argument("cacc")
        ip = self.get_argument("oip")
        osales = self.get_argument("osales")
        mloca = self.get_argument("mloca") #idc location
        pmtype = self.get_argument("pmsource")#payment type
        #add to financial/machine/sub order log
        sosql = "insert into llidc_suborders (s_m_o_id,s_o_details,s_o_pm,s_o_ip,s_o_wsales,s_o_cacc,s_o_memo,s_pm_type) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        soval = (mid,stype,spm,ip,osales,cacc,smemo,pmtype)
        slastid =self.db.insertone(sosql,soval)
        #add to financial log
        otype = '2'
        flsql = "insert into llidc_financial_log(f_o_id,f_o_ip,f_c_acc,f_sales,f_amount,f_otype,f_stype,f_memo,f_idc_loca,f_pm_type) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        flval = (slastid,ip,cacc,osales,spm,otype,stype,smemo,mloca,pmtype)
        flrs = self.db.insertone(flsql,flval)
        #commission
        sod = stype.split(",")[0]
        com = 0
        if sod == "k" or sod =="l":
            if sod =="k":#
                com = spm*com_config["k"]
            elif sod == "l":
                com = com_config["l"]
            csql = "insert into llidc_commission (com_oid,com_em,com_cacc,com_ptype,com_opm,com_cm,com_rate,com_memo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cval = (slastid,osales,cacc,stype,spm,com,com_config[sod],smemo)
            comrs = self.db.insertone(csql,cval)
        else:
            #write to financial but commission is set to 0
            csql = "insert into llidc_commission (com_oid,com_em,com_cacc,com_ptype,com_opm,com_cm,com_rate,com_memo) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cval = (slastid, osales, cacc, stype, spm, com, 0, smemo)
            comrs = self.db.insertone(csql, cval)
        if slastid and flrs and comrs:
            return self.finish(json_encode({"rs": "1038"}))  # successfully add the record
        else:
            return self.finish(json_encode({"rs": "1039"}))  # fail to add the record

class adminFinancialHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        """join machines and orders table"""
        offset = int(self.get_argument("offset", "1")) - 1
        sales = self.get_argument("sid","")#which sales
        oid = self.get_argument("oid","")#oid
        ptype = self.get_argument("ptype","")  # service type
        ips = self.get_argument("ips", "")  # which ip
        u_acc = self.get_argument("u_acc", "")  # client account
        sdt = self.get_argument("sdt","")#start from
        edt = self.get_argument("edt","")#end at
        sql = "select * from llidc_financial_log f join llidc_commission c on c.com_oid = f.f_o_id"
        csql = "select count(*) from llidc_financial_log f join llidc_commission c on c.com_oid = f.f_o_id"
        condition = "1"
        field = "f.f_id"
        num = 20
        if sales:
            condition += " and f.f_sales regexp '%s'"%sales
        if oid:
            condition += " and f.f_o_id regexp '%s'" % oid
        if ips:
            condition += " and f.f_o_ip regexp '%s'" % ips
        if u_acc:
            condition += " and binary f.f_c_acc regexp '%s'" % u_acc
        if ptype:
            condition += " and f.f_stype regexp '%s'"%ptype.split(',')[0]
        if sdt:
            condition += " and f.f_log_dt > '%s'" % sdt
        if edt:
            condition += " and f.f_log_dt < '%s'"%edt
        # print count
        count = self.db.where(condition).getsum(csql)  # total num of orders
        if not count:
            return self.render("admin/admin_financial.html", flogs='', count='', active="financial", pages='',
                               offset='', ctype=self.ctype,eid=self.eid, stype=ptype, u_acc=u_acc, ips=ips, sdt=sdt, edt=edt,
                               sid=sales, oid=oid)
        if count and count % num == 0:
            pages = count // num
        elif count and count % num !=0:
            pages = count // num + 1
        flogs = self.db.where(condition).orderby(field, "desc").limit((offset) * 13, num).getmany(sql)
        return self.render("admin/admin_financial.html", flogs=flogs, count=count, active="financial", pages=pages,offset=offset + 1, ctype=self.ctype, eid=self.eid,stype=ptype, u_acc=u_acc, ips=ips, sdt=sdt,edt=edt,sid=sales,oid=oid)

    @tornado.web.authenticated
    def post(self):
        pass

class adminStatisticsHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        cmonth = dt.now().month
        lmonth = 12 if cmonth == 1 else cmonth - 1
        almonth = "0"+str(cmonth - 1) if len(str(cmonth - 1)) == 1 else str(cmonth - 1)
        cyear = dt.now().year
        lyear = cyear - 1 if cmonth == 1 else cyear
        cmax = calendar.monthrange(cyear,cmonth)[1]
        ss = []
        cymmax = dt.strftime(dt.now(),"%Y-%m")+"-%d"%cmax
        cymmin = dt.strftime(dt.now(),"%Y-%m")+"-01"
        lymmax = str(lyear)+"-"+almonth+"-"+str(calendar.monthrange(lyear,lmonth)[1])
        lymmin = str(lyear)+"-"+almonth+ "-"+"01"
        csql = "select sum(f_amount) from llidc_financial_log"
        lm_cond = "f_log_dt between '%s' and '%s'"%(lymmin,lymmax)
        tm_cond = "f_log_dt between '%s' and '%s'"%(cymmin,cymmax)
        cmsql = "select sum(com_cm) from llidc_commission"
        tcmcond = "com_dt between '%s' and '%s'"%(cymmin,cymmax)
        tcmcond += " and com_em regexp "
        lm_cond += " and f_sales regexp "
        tm_cond += " and f_sales regexp "
        for i in em_sales.keys():
            #print i
            ecm = self.db.where(tcmcond + i).getsum(cmsql)
            lmsum = self.db.where(lm_cond + i).getsum(csql)
            tmsum = self.db.where(tm_cond + i).getsum(csql)
            ss.append({"tmsum":tmsum,"name":em_sales[i],"lmsum":lmsum,"ecm":ecm,"percent":str((tmsum-lmsum)/lmsum*100)+"%"}) if tmsum and lmsum and ecm else ""
        ss.sort(key=lambda x:x['tmsum'],reverse=True)
        return self.render("admin/admin_statistics.html",active="statistics",ss = ss,ctype = self.ctype,eid=self.eid)

class adminFinancialEditHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.send_error(403)
    @tornado.web.authenticated
    def post(self):
        comid = self.get_argument("comid")#commission id
        comval = self.get_argument("comval")#commission value
        csql = "update llidc_commission set com_cm = '%s'"%comval
        ccond = "com_id = '%s'"%comid
        crs = self.db.where(ccond).updateone(csql)
        if crs:
            return self.finish(json_encode({"rs":"1040"}))#successfully modify the commission
        else:
            return self.finish(json_encode({"rs": "1041"}))  # successfully modify the commission

class adminClientsHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        offset = int(self.get_argument("offset","1"))-1
        ctype = self.get_argument("ctype", "")  # if placed order
        cacc = self.get_argument("cacc", "")  # service type
        rname = self.get_argument("rname", "").encode("utf-8")  # service type
        mobile = self.get_argument("mobile", "")  # which ip
        wsales = self.get_argument("wsales", str(self.eid) + ',' + self.uname)  # which sales'order
        qq = self.get_argument("qq", "")  # client account
        sql = "select * from llidc_clients"
        csql = "select count(*) from llidc_clients"
        condition = "1"
        num = 20
        field = "c_acc"
        if ctype == "1":
            sql = "select * from llidc_clients c join llidc_financial_log f on f.f_c_acc = c.c_acc"
            csql = "select count(*) from llidc_clients c join llidc_financial_log f on f.f_c_acc = c.c_acc"
            condition += " and f.f_c_acc is null"

        if cacc:
            condition += " and c_acc '%s'" % cacc
        if rname:
            condition += " and c_real_name = '%s'" % rname
        if mobile:
            condition += " and c_mobile '%s'" % mobile
        if qq:
            condition += " and f_log_dt > '%s'" % qq
        if wsales:
            condition += " and c_belongsto regexp '%s'" % wsales.split(',')[0]
        if not self.ctype in [5]:#admin check all clients
            condition += " and c_belongsto regexp '%s'"%self.eid
        if ctype == "2":#check unbound clients
            condition += " and c_belongsto is null"
        count = self.db.where(condition).getsum(csql)  # total num of orders
        if not count:
            return self.render("admin/admin_clients.html", cs="", count=count, pages="", active="clients",
                               offset="", ctype=self.ctype, eid=self.eid,cacc=cacc, rname=rname, mobile=mobile, qq=qq,wsales=wsales)
        if count and count % num == 0:
            pages = count // num
        elif count and count % num != 0:
            pages = count // num + 1

        if ctype == "1":
            cs = self.db.orderby(field, "desc").limit((offset) * 13, num).getmany(sql+condition)
        else:
            cs = self.db.where(condition).orderby(field, "desc").limit((offset) * 13, num).getmany(sql)
        return self.render("admin/admin_clients.html", cs=cs, count=count, pages = pages,active="clients",offset = offset+1,ctype=self.ctype, eid=self.eid,cacc=cacc, rname=rname, mobile=mobile, qq=qq,wsales=wsales)

    @tornado.web.authenticated
    def post(self):
        pass


class clientRemoveHandler(baseHandler):
    @tornado.web.authenticated
    def post(self,cid):
        rmsql = "delete from llidc_clients"
        cond = "c_id = '%s'"%cid
        csql ="select * from llidc_clients c join llidc_financial_log f on f.f_c_acc = c.c_acc"
        cex = self.db.where(cond).checkIfExist(csql)
        if cex:
            #client has order record
            return self.finish(json_encode({"rs":"1057"}))#can't remove client
        else:
            rs = self.db.where(cond).remove(rmsql)
            if rs:
                return self.finish(json_encode({"rs": "1055"})) #successfully remove client
            else:
                return self.finish(json_encode({"rs": "1056"}))#fail to remove client

class clientModifyHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.send_error(403)

    @tornado.web.authenticated
    def post(self):
        cid = self.get_argument("cid","")
        rname = self.get_argument("rname","")
        mobile = self.get_argument("mobile","")
        idc = self.get_argument("idc","")#id card num
        qq = self.get_argument("qq","")#qq number
        memo = self.get_argument("memo","")
        add = self.get_argument("add","")
        udsql = "update llidc_clients set c_real_name = '%s',c_mobile = '%s',c_id_card = '%s',c_qq = '%s',c_memo = '%s',c_address = '%s'"%(rname,mobile,idc,qq,memo,add)
        cond = "c_id = '%s'"%cid
        rs = self.db.where(cond).updateone(udsql)
        if rs:
            return self.finish(json_encode({"rs":"1059"}))#successfully modify the client details
        else:
            return self.finish(json_encode({"rs": "1060"}))  # successfully modify the client details

class adminResetPwdHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        if self.ctype in [3, 4, 5]:
            return self.render("admin/admin_modify_pwd.html",ctype=self.ctype,uname=self.uname,active = "index",eid = self.eid)
        else:
            self.send_error(403)

    @tornado.web.authenticated
    def post(self):
        eid = self.get_argument("eid")#employee id
        opwd = self.get_argument("opwd")#original password
        unpwd = self.get_argument("unpwd")#new pwd
        unrpwd = self.get_argument("unrpwd")#confirm pwd
        csql = "select u_pwd from llidc_employees"
        ccond = "u_id = '%s'"%eid
        opwded2 = self.db.where(ccond).getone(csql)[0]
        o = hashlib.md5()
        o.update(opwd+'llidc')
        opwded1 = o.hexdigest()
        if opwded1 == opwded2:
            if unpwd == unrpwd:
                m = hashlib.md5()
                m.update(unpwd+"llidc")
                unrpwded = m.hexdigest()
                upsql = "update llidc_employees set u_pwd = '%s'"%unrpwded
                rs = self.db.where(ccond).updateone(upsql)
                if rs:
                    return self.redirect("/admin/mpredirect/")
                else:
                    self.send_error(403)
            else:
                self.send_error(403)
        else:
            self.send_error(403)

class adminMpRedirectHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("admin/admin_pwd_redirect.html",active="index",ctype=self.ctype,eid= self.eid)

class adminModifyPwdRedirectHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("admin/admin_mpresult.html",active="index",ctype=self.ctype,eid= self.eid)

class adminClientBindHandler(baseHandler):
    @tornado.web.authenticated
    def post(self):
        cid = self.get_argument("cid")
        sales = self.get_argument("sales")
        udsql = "update llidc_clients set c_belongsto = '%s'"%(sales)
        udcond = "c_id = '%s'"%cid
        rs=self.db.where(udcond).updateone(udsql)
        if rs:
            return self.finish(json_encode({"rs":1061})) #added client
        else:
            return self.finish(json_encode({"rs": 1062}))#fail

class adminAddHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        if self.ctype in [3,4,5]:
            return self.render("admin/admin_add.html",**{"ctype":self.ctype,"eid":self.eid,"active":"index"})
        else:
            self.send_error(403)

    @tornado.web.authenticated
    def post(self):
        uacc = self.get_argument("uacc")
        upwd = self.get_argument("unpwd")
        unrpwd = self.get_argument("unrpwd")
        ctype = self.get_argument("ctype")
        rname = self.get_argument("rname")
        if upwd == unrpwd:
            m= hashlib.md5()
            m.update(upwd+"llidc")
            upwded = m.hexdigest()
            sql = "insert into llidc_employees (u_acc,u_name,u_pwd,u_type) values(%s,%s,%s,%s)"
            values = (uacc,rname,upwded,ctype)
            rs = self.db.insertone(sql,values)
            if rs:
                return self.redirect("/admin/addredirect/")
            else:
                self.send_error(404)
        else:
            self.send_error(403)

class adminAddRedirectHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("admin/admin_addredirect.html",ctype=self.ctype,eid=self.eid,active="index")

class adminAddSuccessHandler(baseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("admin/admin_addsuccess.html",ctype=self.ctype,eid=self.eid,active="index")

#*********************************************************************************************client part
class clientBaseHandler(baseHandler):
    def __init__(self,application,*args, **kwds):
        tornado.web.RequestHandler.__init__(self, application,*args, **kwds)
        self.ua = self.request.headers.get("User-Agent")
        self.path = self.request.uri
        x_real_ip = self.request.headers.get("X-Real-IP")
        self.remote_ip = x_real_ip or self.request.remote_ip  # when use nginx we get x_real_ip or we just get remote_ip

    def get_current_user(self):
        """{current_user} in template,request:self.current_user"""
        return self.get_secure_cookie("_c")

    def get_login_url(self):
        return '/client/auth/'

class clientAuthHandler(clientBaseHandler):
    def get(self):
        if self.get_secure_cookie("_c"):
            active = "index"
            return self.redirect("/client/mypanel/")
        imgc = webCaptcha()
        imglist = imgc.saveImg()
        thiscc = imglist[1]  # 当前的验证码
        self.set_secure_cookie("cc",thiscc,expires_days=1)
        return self.render("client/client_auth.html",acc=imglist[0])

    def post(self):
        uacc = self.get_argument("uacc")
        upwd = self.get_argument("upwd")
        sql = "select * from llidc_clients"
        cond = "c_acc = '%s' or c_mobile = '%s'" % (uacc, uacc)
        rs = self.db.where(cond).getone(sql)
        if rs:
            m = hashlib.md5()
            m.update(upwd + "clientllidc")
            upwded = m.hexdigest()
            if rs[4] == upwded:
                self.set_secure_cookie("_c", rs[1])
                next = self.get_argument("next", "")
                if next:
                    return self.redirect(next)  # rediret to the previous url
                return self.redirect("/client/lgredirect/")
            else:
                self.send_error(403)
        else:
            self.send_error(404)

#send message when client login
class clientMsgHandler(clientBaseHandler):
    @tornado.web.asynchronous
    def get(self):
        self.phone = self.get_argument("phone","")
        asyncClient = AsyncHTTPClient()
        turl = msg_config['turl']
        params = {
        "mobile" : self.phone, #接收短信的手机号码
        "tpl_id" : msg_config['model'], #短信模板ID，请参考个人中心短信模板设置
        "tpl_value" : "#code#="+baseHandler.getnum(6), #变量名和变量值对。如果你的变量名或者变量值中带有#&amp;=中的任意一个特殊符号，请先分别进行urlencode编码后再传递，&lt;a href=&quot;http://www.juhe.cn/news/index/id/50&quot; target=&quot;_blank&quot;&gt;详细说明&gt;&lt;/a&gt;
        "key" : msg_config["appkey"], #应用APPKEY(应用详细页查询)
        "dtype" : "json", #返回数据的格式,xml或json，默认json
        }
        url = url_concat(turl, params)
        asyncClient.fetch(url,self.handle_callback)

    def handle_callback(self,response):
        #print response.effective_url
        if response.code == msg_config['scode']:
            #log to mysql
            pat = re.compile("tpl_value=(.*)")
            #print pat.search(response.effective_url).group(1)
            tpl_value=pat.search(response.effective_url).group(1)
            code = tpl_value[-6:len(tpl_value)]
            sql = "insert into llidc_message (m_msg,m_phone,m_ip,m_ua,m_cpath) values (%s,%s,%s,%s,%s)"
            values = (code,self.phone,self.remote_ip,self.ua,self.path)
            rs = self.db.insertone(sql,values)
            if rs:
                return self.finish(json_encode({"rs":"1050",'msgid':rs}))#successfully send the msg to user
        else:
            return self.finish(json_encode({"rs": "1051"}))  # fail to send the msg to user

    @tornado.web.authenticated
    def post(self):
        pass

class clientRegHandler(clientBaseHandler):
    def get(self):
        if self.get_secure_cookie("_c"):
            active = "index"
            return self.redirect("/client/mypanel/")
        imgc = webCaptcha()
        imglist = imgc.saveImg()
        thiscc = imglist[1]  # 当前的验证码
        self.set_secure_cookie("cc",thiscc,expires_days=1)
        return self.render("client/client_reg.html",acc=imglist[0])

    def post(self):
        uacc = self.get_argument("uacc")#user account ,6 nums
        mobile = self.get_argument("mobile")#mobile
        pwd = self.get_argument("unpwd")#password
        #checking msg cc
        m=hashlib.md5()
        m.update(pwd+'clientllidc')
        pwded = m.hexdigest()
        sql = "insert into llidc_clients (c_acc,c_pwd,c_mobile) values(%s,%s,%s)"
        values = (uacc,pwded,mobile)
        rs=self.db.insertone(sql,values)
        if rs:
            #write to cookie
            self.set_secure_cookie("_c",uacc)
            next = self.get_argument("next", "")
            if next:
                return self.redirect(next)  # rediret to the previous url
            return self.redirect("/client/redirect/")
        else:
            self.send_error(404)

class clientCheckmsgHandler(clientBaseHandler):
    def get(self,mid):
        msgcc = self.get_query_argument("msgcc")
        csql = "select m_msg from llidc_message"
        ccond = "m_id = '%s'" % mid
        mrs = self.db.where(ccond).getone(csql)[0]
        if mrs == msgcc:
            return self.finish(json_encode({"cre":"0"}))#0 is positive response
        else:
            return self.finish(json_encode({"cre":"1"}))

class clientCheckMobileHandler(clientBaseHandler):
    def get(self,mnum):
        csql = "select * from llidc_message"
        ccond = "m_phone = '%s'" % mnum
        mrs = self.db.where(ccond).checkIfExist(csql)
        if mrs:
            return self.finish(json_encode({"cre":"1"}))
        else:
            return self.finish(json_encode({"cre":"0"}))

class clientRedirectHandler(clientBaseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("client/client_redirect.html",active="orders")

class clientLgredirectHandler(clientBaseHandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("client/client_lgredirect.html",active="orders")

class clientPanelHandler(clientBaseHandler):
    @tornado.web.authenticated
    def get(self):
        ips = self.get_argument("ips","")
        sdt = self.get_argument("sdt","")
        edt = self.get_argument("edt","")
        oid = self.get_argument("oid","")
        offset = int(self.get_argument("offset",1))-1
        sql = "select * from llidc_orders o join llidc_clients c on o.o_c_acc = c.c_acc join llidc_machines m on o.o_ip = m.m_ip"
        csql = "select sum(*) from llidc_orders o join llidc_clients c on o.o_c_acc = c.c_acc join llidc_machines m on o.o_ip = m.m_ip"
        cond = "o_c_acc = '%s'"%self.get_secure_cookie("_c")
        count = self.db.where(cond).getsum(sql)
        num = 13
        field = 'o_id'
        if not count:
            return self.render("client/client_mypanel.html", orders='', count='', active="orders", pages='',offset='',ips=ips, sdt=sdt,
                               edt=edt, oid=oid)
        if count and count % num == 0:
            pages = count // num
        elif count and count % num != 0:
            pages = count // num + 1
        orders = self.db.where(cond).orderby(field, "desc").limit((offset) * 13, num).getmany(sql)
        return self.render("client/client_mypanel.html", orders=orders, count=count, active="orders", pages=pages,
                           offset=offset + 1,ips=ips,sdt=sdt, edt=edt, oid=oid)

class clientQuitHandler(clientBaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.clear_cookie("_c")
        self.clear_cookie("_cac")
        self.redirect("/")
























