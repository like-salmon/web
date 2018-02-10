#!/usr/bin/python
# coding:utf-8

"""
put this file in directory spider of llidc.com
"""

from pyquery import PyQuery as pq
import random, re, os, time, MySQLdb, urllib2

baseurl = "http://www.wy.cn/"
nlist = ".dynamic-content ul li dd a"

# mysql settings
ds = {
    "host": 'localhost',
    'port': 3306,
    'user': 'root',
    'db': 'llidc',
    'passwd': "080826@zxgj"
}

# ua
ua = random.choice([
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Baiduspider',
    'Baidu Web Search',
    'Baidu Image Search',
    'Baiduspider-image',
    'Baidu Mobile Search',
    'Baiduspider-mobile',
    'Baidu Video Search',
    'Baiduspider-video',
    'Baidu News Search',
    'Baiduspider-news',
    'Baidu Bookmark Search',
    'Baiduspider-favo',
    'Baidu Union Search',
    'Baiduspider-cpro',
    'Baidu Business Search',
    'Baiduspider-ads',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Baiduspider+(+http://www.baidu.com/search/spider_jp.html)',
    'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
])

headers = {'User-Agent': ua}
req = urllib2.Request(baseurl, None, headers)
html = pq(urllib2.urlopen(req).read())
lists = html(".ui-dynamic").find(nlist)
db = MySQLdb.connect(host=ds["host"], port=ds["port"], user=ds["user"], passwd=ds["passwd"], db=ds["db"],
                     charset="utf8")
cur = db.cursor()
mpath = os.path.join("/".join(os.path.dirname(__file__).split("/")[0:len(os.path.dirname(__file__).split("/")) - 1]),
                     "static/img/news")

if os.name == "nt":
    mpath = os.path.join(
        "\\".join(os.path.dirname(__file__).split("\\")[0:len(os.path.dirname(__file__).split("\\")) - 1]),
        "static\\img\\news")

# 当前的路径
ctime = str(int(time.time()))
cpath = os.getcwd()
os.chdir(mpath)
os.mkdir(ctime)
os.chdir(ctime)

for i in range(2, len(lists)):
    nurl = lists.eq(i).attr("href")[1:]
    req = urllib2.Request(baseurl + nurl, None, headers)
    html = pq(urllib2.urlopen(req).read())
    title = html.find(".newsDetail h2").text().encode("utf-8").replace("唯一", "利联")
    pdate = html.find(".newsDetail .newsDate span").text()
    content = html.find(".newsDetail .newsContent").html().encode("utf-8").replace("唯一", "利联")
    # 处理图片
    imgs = html.find(".newsDetail .newsContent img")
    if imgs:
        for i in range(0, len(imgs)):
            mlink = imgs.eq(i).attr("src")
            # 后缀
            print "processing img:", "http:" + mlink
            exten = mlink.split(".")[-1]
            mreq = urllib2.Request("http:" + mlink, None, headers)
            imgc = urllib2.urlopen(mreq).read()
            imgname = ctime + "-" + random.choice(
                [chr(i) for i in range(1, 256) if chr(i).isdigit() or chr(i).isalpha()]) + "-" + random.choice(
                list("llidcnewsimg")) + "." + exten
            cmlink = "img/news/" + ctime + "/" + imgname
            # print cmlink
            with open(imgname, "wb") as f:
                f.write(imgc)
            # set new img path
            print imgs.eq(i).attr("src")
            print "current image src is:", imgs.eq(i).attr("src")

    print "processed all imgs."
    os.chdir(cpath)

    fields = "(n_title,n_content,n_datetime)"
    values = (fields, title, content, pdate)
    sql = "insert into llidc_news %s values('%s','%s','%s')" % values
    result = cur.execute(sql)
    db.commit()
    print "inserted into llic_news table,news title is:", title

cur.close()
