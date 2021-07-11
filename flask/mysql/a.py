import mysql.connector
conn = mysql.connector.connect( host="192.168.202.154", port="3303", user='root', password='yf3b@abc123', database='spug')
cursor = conn.cursor()
cursor.execute('create table t_user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into t_user (id, name) values (%s, %s)', ['1', 'Michael'])
conn.commit()
cursor.close()
cursor = conn.cursor()
cursor.execute('select * from t_user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()