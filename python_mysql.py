import pymysql
# 打开数据库连接
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='root',
    db='world',
    charset='utf8')
# 创建游标对象
cur = conn.cursor()
# 执行sql语句
cur.execute('select * from city ')
# 接收全部的返回结果行，是一个truple

set = cur.fetchone()
print(set)  # 结果返回第m列数据
# 获取下一个查询结果集，结果集是一个对象
# set2=cur.fetchall()
# 结果返回第n条数据的全部信息
# print(set2[0])
# 结果返回第n条数据的第m列的数据
print(set[1])

try:
    # 执行sql语句
    cur.execute("update city set Name='wwj2' where ID=1 ")
    # 提交到数据库执行
    conn.commit()
    # 返回影响的行数，只读
    print(cur.rowcount)
except BaseException:
    # 如果发生错误则回滚
    conn.rollback()
# 关闭游标指针
cur.close()
# 关闭数据库连接
conn.close()
