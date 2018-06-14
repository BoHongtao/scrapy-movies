import pymysql.cursors
from movies import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
MYSQL_CHARACTERS = settings.MYSQL_CHARACTERS

# 获取游标
connect = pymysql.Connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB,charset=MYSQL_CHARACTERS)
cur = connect.cursor()
class Sql:
    @classmethod
    def insert(cls,movie_name, movie_info,movie_download):
        sql = "INSERT INTO movie (id,movie_name,movie_info,movie_download) VALUES ( '%s', '%s', '%s' ,'%s')"
        value = ('0',movie_name, movie_info,movie_download)
        cur.execute(sql % value)
        connect.commit()