#-*-coding:utf8-*-
import MySQLdb

def connectdb(searchSql,choosedb):
    db=MySQLdb.connect(host="172.16.21.23",user="cloud_test",passwd="test_cloud14425",db=choosedb,port=3306,charset='utf8')
    cursor=db.cursor()
    cursor.execute(searchSql)
    #修改数据，一定要写下面的提交语句
    db.commit()
    searchData = cursor.fetchall()
    return searchData
