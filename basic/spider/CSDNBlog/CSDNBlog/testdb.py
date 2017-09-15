import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='mysql', port=3306)
    cur = conn.cursor()


    cur.execute('create database if not exists PythonDB')
    conn.select_db('PythonDB')
    cur.execute('create table Test(id int,name varchar(20),info varchar(20))')


    value = [1, 'ACdreamer', 'student']
    cur.execute('insert into Test values(%s,%s,%s)', value)

    values = []
    for i in range(20):
        values.append((i, 'Hello World!', 'My number is ' + str(i)))

    cur.executemany('insert into Test values(%s,%s,%s)', values)
    cur.execute('update Test set name="ACdreamer" where id=3')

    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error, msg:
    print "MySQL Error %d: %s" % (msg.args[0], msg.args[1])