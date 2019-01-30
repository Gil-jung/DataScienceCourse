import pymysql.cursors
import pandas as pd
import numpy as np

def f1():
    # DB상의 모든 학생들의 이름과 주민등록번호를 출력
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT name, resident_id FROM student"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()

    df = pd.DataFrame(result)
    print(df)