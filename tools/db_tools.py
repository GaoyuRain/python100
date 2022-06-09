"""
author :admin
Date : 2021/08/13
Description : 数据库操作
"""
import pymysql

from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin
from configparser import ConfigParser
from sshtunnel import SSHTunnelForwarder


# import MySQLdb

class DBTools:
    DB = 'easyprd_fat'
    host = '192.168.215.254'
    user = 'easyprd_fat_rw'
    pwd = 'pYGUt1O8cdbgvkEz0Va9Fy57'

    #
    # DB = 'easyprd_dev'
    # host = '10.39.201.254'
    # user = 'easyprd_dev_rw'
    # pwd = 'pYGUt1O8cdbgvkEz0Va9Fy57'

    @staticmethod
    def connection_db():
        connect = pymysql.connect(host=DBTools.host, port=3306, db=DBTools.DB,
                                  user=DBTools.user, password=DBTools.pwd, ssl_verify_identity=False)
        cur = connect.cursor()
        sql = '''select * from reqment WHERE create_user="高雨" '''
        cur.execute(sql)
        res: tuple = cur.fetchall()
        print(type(res))
        for i in res:
            print(i)

    _instance = None

    @staticmethod
    def get_db_instance():
        server = SSHTunnelForwarder(
            ssh_address_or_host='10.39.203.6',
            ssh_port=1194,
            ssh_password='',
            ssh_username='xaxzsre',
            remote_bind_address=('192.168.215.254', 3306))
        server.start()
        DBTools.connection_db()


if __name__ == '__main__':
    DBTools.get_db_instance()
