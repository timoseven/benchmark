#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
from sqlalchemy import types
from sqlalchemy.dialects.mysql.base import MSBinary
from sqlalchemy.schema import Column
import uuid



# 打开数据库连接
db = MySQLdb.connect("localhost","root","","chatmessage_test" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

for i in xrange(0, 100000):
    # SQL 插入语句
#    sql = "INSERT INTO chatmessage(msgId, tenantId, messageType, fromUserId, toUserId, contentType, body, chatGroupSeqId, sessionServiceSeqId, createDateTime, timestamp, chatGroupId, sessionServiceId, year, month, day, hour, year_month_day, fromuser_userId, fromuser_userType, fromuser_nicename, touser_userId, touser_userType, touser_nicename)  VALUES ('%s', '%d', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s',  '%d', '%s', '%d', '%d', '%d', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%s')"
#    sql = "INSERT INTO chatmessage (msgId, tenantId, messageType, fromUserId, toUserId, contentType, body, chatGroupSeqId, sessionServiceSeqId, createDateTime, timestamp, chatGroupId, sessionServiceId, year, month, day, hour, year_month_day, fromuser_userId, fromuser_userType, fromuser_nicename, touser_userId, touser_userType, touser_nicename)  VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',  '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
    sql = 'INSERT INTO chatmessage VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    param = (str(uuid.uuid4()), int(i), 'NULL', str(uuid.uuid4()), '_1', 'NULL', '{"bodies":[{"msg":"我爱死哈利波特了","type":"txt"}],"ext":{"weichat":{"msgId":"00000000-90f0-4921-977e-1f2dd38e151f","from":"p130057745","to":"xuebaother","channelType":"easemob","timestamp":1478321398780,"tenantId":10846,"serviceSessionId":"e68d9561-354f-4d03-91f4-0a9f091e1c6a","visitorUserId":"7901f2b6-eaba-45a5-9541-37857fa513e3","originType":"app","to_jid":"wenba100#xuebajun_xuebaother@easemob.com","msg_id":"260947604542588928","channel_id":23677,"channel_name":"其它"}', int(i), int(i), '2016-11-05 12:49:59.035090', '2016-11-05 12:49:59.035090', int(i), str(uuid.uuid4()), 2016, 11, 5, 12, 20161105, str(uuid.uuid4()), 'Visitor', 'p130057745', '_1', 'ALL', 'ALL')

    try:
       # 执行sql语句
#       print(sql, param)
       cursor.execute(sql, param)
       # 提交到数据库执行
       db.commit()
    except Exception as e:
       print e
       # 发生错误时回滚
       db.rollback()

# 关闭数据库连接
db.close()
