import pymysql


def middle():
    con_engines = pymysql.connect(host='8.142.138.101',
                                  user="root",
                                  password="0552fe7ad2067bda",
                                  database="database",
                                  port=3306,
                                  charset='utf8',
                                  cursorclass=pymysql.cursors.DictCursor)
    cursor = con_engines.cursor()
    sql = "select title from policy where title LIKE '%国家%'"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

if __name__ == '__main__':
    middle()