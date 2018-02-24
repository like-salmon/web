#!/usr/bin/ python
# coding:utf-8

import MySQLdb, time, datetime
from config.settings import dbsettings as ds

__metaclass__ = type

class dbWrapper():
    """mysql CRUD operation"""
    def __init__(self):
        # super(dbWrapper,self).__init__()
        self.cond = ' where 1 '
        self.database = MySQLdb.connect(host=ds["host"], port=ds["port"], user=ds["user"], passwd=ds["passwd"], db=ds["db"],use_unicode=1,charset="utf8")
        self.database.ping(True)#auto reconnect on mysql server's gone away
        self.cur = self.database.cursor()
        self.order = ''
        self.sql = ''
        self.offset = ''  # which record from
        self.page = ''  # how many records,-1 means till the last record

    def where(self, condition):
        if condition:
            self.cond += "and " + condition
        return self

    def orderby(self, field, order="asc"):
        if not self.order:
            self.order = ' order by ' + field + " " + order
        else:
            self.order += ","+field+" "+ order

        return self

    def limit(self, offset, page=''):
        self.offset = str(offset)
        self.page = str(page)
        return self

    def getone(self, sql):
        self.sql = sql + self.cond
        if self.order:
            self.sql += self.order
        if self.offset and not self.page:
            self.sql += " limit %s" % self.offset
        if self.offset and self.page:
            self.sql += " limit %s,%s" % (self.offset, self.page)
        try:
            #print self.sql
            self.cur.execute(self.sql)
            self.database.commit()
            results = self.cur.fetchone()
            return results
        except Exception as e:
            print "encountered error when get one record from mysql:", e
        finally:
            self.cond = ' where 1 '
            self.order = ''
            self.offset = ''
            self.page = ''
            self.sql = ''

    def getmany(self, sql):
        self.sql = sql + self.cond
        if self.order:
            self.sql += self.order
        if self.offset and not self.page:
            self.sql += " limit %s" % self.offset
        if self.offset and self.page:
            self.sql += " limit %s,%s" % (self.offset, self.page)
        try:
            #print self.sql
            self.cur.execute(self.sql)
            self.database.commit()
            results = self.cur.fetchall()
            return results
        except Exception as e:
            print "encountered error when get records from mysql:", e
        finally:
            self.cond = ' where 1 '
            self.order = ''
            self.offset = ''
            self.page = ''
            self.sql = ''


    def insertone(self, sql,values):
        #print sql,values
        try:
            self.cur.execute(sql,values)
            self.database.commit()
            return self.cur.lastrowid#return the last insert id
        except Exception as e:
            print "encountered error when insert into db", e
            self.database.rollback()

    def updateone(self, sql):
        '''update table set col1 = a,col2 = b,col3 = c where cond order by *'''
        try:
            print sql + self.cond
            n=self.cur.execute(sql + self.cond)
            self.database.commit()
            return n
        except Exception as e:
            print "encountered error when update db", e
            self.database.rollback()
            return 0
        finally:
            self.cond = ' where 1 '

    def getsum(self,sql):
        self.sql = sql + self.cond
        #print self.sql
        try:
            self.cur.execute(self.sql)
            self.database.commit()
            num = self.cur.fetchone()
            return num[0]
        except Exception as e:
            print "encountered error when get summary data from mysql:", e
        finally:
            self.cond = ' where 1 '
            self.sql = ''
            self.order = ''

    def remove(self,sql):
        "delete from zxgj_users where u_Id = 1;"
        self.sql = sql
        try:
            rs=self.cur.execute(self.sql+self.cond)
            self.database.commit()
            return rs
        except Exception as e:
            print "encountered error when delete record from table",e
            self.database.rollback()
            return 0
        finally:
            self.sql = ""
            self.cond = ' where 1 '

    def checkIfExist(self,sql):
        """check if record exists"""
        self.sql = sql + self.cond
        try:
            #print self.sql
            self.cur.execute(self.sql)
            results = self.cur.fetchone()
            self.database.commit()
            if results and len(results):
                return 1
            else:
                return 0
        except Exception as e:
            print "encountered error when get one record from mysql:", e
        finally:
            self.sql = ""
            self.cond = ' where 1 '

    def clean(self):
        """this method is used for cleaning up the clients who send no periodical request to websocket """
        ts = datetime.datetime.fromtimestamp(time.time()-10).strftime('%Y-%m-%d %H:%M:%S')#clean
        sql = "update llidc_visiters set v_ing = 0 where v_ts < '%s' and v_ing = '1'"%ts
        cts = datetime.datetime.fromtimestamp(time.time() - 3600*12).strftime('%Y-%m-%d %H:%M:%S')  # clean yesterday's data
        csql = "delete from llidc_visiters where v_ts <= '%s'"%cts
        try:
            self.cur.execute(sql)
            self.cur.execute(csql)
            self.database.commit()
            #return 1
        except Exception as e:
            print "encountered error when delete record from table",e
            self.database.rollback()
            #return 0

    def __del__(self):
        self.cur.close()
        self.database.close()


if __name__ == "__main__":
    db = dbWrapper()
    sql = "select * from llidc_admin_users"
    user = db.where("a_Id = 1").fetchone(sql)
    print user









