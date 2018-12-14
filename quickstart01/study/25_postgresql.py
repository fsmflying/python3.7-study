#!/usr/bin/python3
import psycopg2

vhost = input("请输入数据库服务器地址[localhost]:");
if vhost == "":
    vhost = "localhost"

vport = input("请输入数据库服务器端口[5432]:");
if vport == "":
    vport = 5432
else:
    vport = int(vport)

vuser = input("请输入连接数据库的用户[postgres]:");
if vuser == "":
    vuser = "postgres"
vpassword = input("请输入连接数据库的密码[fangming]:");
if vpassword == "":
    vpassword = "fangming"

vdatabase = input("请输入连接的数据库[mix]:");
if vdatabase == "":
    vdatabase = "mix"

conn =psycopg2.connect(host=vhost,port=vport,user=vuser,password=vpassword,database=vdatabase)
cur = conn.cursor()

sqlTables = '''
select * from pg_tabels where 
'''

cur.close()