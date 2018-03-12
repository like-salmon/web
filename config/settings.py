#!/usr/bin/env python
#coding:utf-8

import os
from template import wmodules

#tornado setting
websettings={
"template_path": os.path.join(os.path.dirname(__file__), "../template"),
"static_path": os.path.join(os.path.dirname(__file__), "../static"),
"cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
"xsrf_cookies": True,
"login_url": "/admin/",
"debug":True,
"op":["李富城"],
"ndir":"D:\\web\\llidc-local\\static\\img\\news\\",#path for saving news images
"tndir":"D:\\mywork\\llidc\\static\\img\\news\\"
}

#mysql settings
dbsettings={
"host":'localhost',
'port':3306,
'user':'root',
'db':'llidc',
'passwd':"zxgj0313"
}

#machines related configuration
machine_status = {"a":"空闲","b":"租用","c":"托管","d":"试用","e":"自用","f":"回收"}
machine_room_number = {"1":"厦门哈曼尼","2":"东莞枫华园","3":"浙江绍兴","4":"浙江杭州","5":"香港机房","6":"美国机房"}
machine_type = {"0":"普通机器","1":"刀片机"}

#order related configuration
order_service_type = {"b":"租用","c":"托管","d":"试用","e":"失效"}
sub_order_type = {"h":"加内存","i":"加硬盘","j":"加IP","k":"加带宽","l":"加防护","m":"其它(请备注具体内容)"}

financial_log = {"o":"续期"}
#fianncial related configuration
order_product_type = {"r":"普通机托管","s":"普通机租用","t":"高防机托管","u":"高防机租用","v":"代理机托管","w":"代理机租用","x":"机柜出租"}
order_renew_type = {"rr":"普通机托管续费","rs":"普通机租用续费","rt":"高防机托管续费","ru":"高防机租用续费","rv":"代理机托管续费","rw":"代理机租用续费","rx":"机柜出租续费"}
#employee's configuration
em_num = {"2":"李富城","3":"袁伟东","4":"杨丰华","18":"劳兴华","19":"陶秋梅","20":"唐晓珍","21":"黄小恩","22":"廖超","23":"闭健龙","25":"可艳","26":"朱总"}
em_sales = {"18":"劳兴华","19":"陶秋梅","20":"唐晓珍","21":"黄小恩","22":"廖超"}
pm_source = {"a":"工商银行","b":"建设银行","c":"支付宝","d":"财富通","e":"微信支付"}
#commission
#一台机器不会有多个订单，要么是单台，要么是机柜
com_config = {"r":50,"s":30,"t":120,"u":120,"v":0.1,"w":0.1,"x":0.05,'k':0.1,'l':50}#对应 order_product_type和sub_order_type
renew_com_config = {"rr":25,"rs":20,"rt":80,"ru":80,"rv":0.1,"rw":0.1,"rx":0.03}#renew order,add bandwidth,add defence is not took into consideration

#msg API
msg_config = {"appkey":"e0e03607cd0f7104795aab39a6cee8d6",#appkey
              "model":"42627",#model number
              "turl":"http://v.juhe.cn/sms/send",#api
              "ecode":205402,#error code
              "scode":200}#when successful code

