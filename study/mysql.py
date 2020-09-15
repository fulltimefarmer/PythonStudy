import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='auth',
    charset='utf8'
)

cursor = conn.cursor()

sql = 'select * from gcsc_user'

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        username = row[2]
        displayName = row[5]
        createDate = row[7]

        print("id=%s, username=%s, displayName=%s, createDate=%s" % (id, username, displayName, createDate))
except BaseException as e:
    print(str(e))
finally:
    cursor.close()
    conn.close()
