#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/8 14:58
# @Author  : Nxy
# @Site    : 
# @File    : dbUtil.py
# @Software: PyCharm
import pymysql
import sys
import  sqlite3
class dbUtil():
    #连接mysql数据库
    def getMysqlConnection(self,db,user,host,passwd,port,charset):
        self.db = db
        self.user=user
        self.host=host
        self.passwd= passwd
        self.port= port
        self.charset = charset
        try:
            self.connection = pymysql.Connect(host=self.host,user=self.user,passwd =self.passwd,db=self.db,charset = self.charset)
            #print'数据库连接成功'
            return self.connection
        except pymysql.Error as e:
            print("Error %d: %s"%(e.args[0],e.args[1]))
            sys.exit(0)

    #sqlite 适合用于  没有database 全部都新开始  如果没有所制定的database他会自己创建一个database
    def getSQLiteConnection(self,db):
        self.db = db
        try:
            self.connection = sqlite3.connect(db)
            print('数据库连接成功')
        except sqlite3.Error as e:
            print("Error %d: %s"%(e.args[0],e.args[1]))
            exit(0)
    #关闭连接
    def closeConn(self,conn):
        self.conn = conn
        cur = conn.cursor()
        cur.close()
        conn.Close()