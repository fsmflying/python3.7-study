#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pymysql

vhost = input("请输入数据库服务器地址[localhost]:");
if vhost == "":
    vhost = "localhost"

vport = input("请输入数据库服务器端口[3306]:");
if vport == "":
    vport = 3306
else:
    vport = int(vport)

vuser = input("请输入连接数据库的用户[root]:");
if vuser == "":
    vuser = "root"
vpassword = input("请输入连接数据库的密码[fangming]:");
if vpassword == "":
    vpassword = "fangming"
vdatabase = input("请输入连接的数据库[mix]:");
if vdatabase == "":
    vdatabase = "mix"

# 打开数据库连接
conn = pymysql.Connect(host=vhost, user=vuser, password=vpassword, database=vdatabase, port=vport)
# db=pymysql.connect(vhost,vuser,vpassword,vdatabase,vport)

# 使用cursor()方法获取操作游标
cur = conn.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sqlTables = '''
select table_name,table_comment 
from information_schema.tables 
where table_schema='{}';
'''
sqlColumns = '''
select column_name,column_comment
from information_schema.columns
where table_schema='{}' and table_name='{}'; 
'''

try:
    cur.execute(sqlTables.format(vdatabase))  # 执行sql语句
    tables = cur.fetchall()  # 获取查询的所有记录
    print("table_name", "table_comment")
    # 遍历结果
    for tableRow in tables:
        table_name = tableRow[0]
        table_comment = tableRow[1]
        print("############################################")
        print(table_name, '\t\t', table_comment)
        cur.execute(sqlColumns.format(vdatabase, table_name))
        columns = cur.fetchall()
        print("---------------")
        for columnRow in columns:
            column_name = columnRow[0]
            column_comment = columnRow[1]
            print(column_name, '\t\t', column_comment)

except Exception as e:
    raise e
finally:
    conn.close()  # 关闭连接
