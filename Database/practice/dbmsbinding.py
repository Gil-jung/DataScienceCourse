import pymysql.cursors
import pandas as pd

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

def f2():
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = ("SELECT p1.name, 2019-p1.year_emp as emp_year "
                   "FROM professor p1, professor p2 "
                   "WHERE p2.name = '최성희' and p1.year_emp > p2.year_emp ")
            cursor.execute(sql)
            result_b = cursor.fetchall()
    finally:
        connection.close()

    df = pd.DataFrame(result_b)
    print(df)

def f3():
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    name = input("학생의 이름을 입력해주세요: ")

    try:
        with connection.cursor() as cursor:
            sql = ("SELECT title, grade "
                   "FROM student natural join takes join class "
                   "on takes.class_id = class.class_id "
                   "natural join course "
                   "WHERE student.name = %s ")
            cursor.execute(sql, name)
            result_c = cursor.fetchall()
    finally:
        connection.close()

    print("이름: ", name)
    # print(result_c)
    df = pd.DataFrame(result_c)
    print(df)