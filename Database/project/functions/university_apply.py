import pymysql.cursors
import pandas as pd

def f1():
    ### print all universities ###
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27_project',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = ("SELECT u_id, u_name, capacity, u_group, cutline, weight "
                   "FROM university "
                   "ORDER BY u_id ")
            cursor.execute(sql)
            # connection.commit()
            result = cursor.fetchall()
    finally:
        connection.close()

    df = pd.DataFrame(result)
    print(df)

def f2():
    ### print all students ###
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27_project',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = ("SELECT * "
                   "FROM student "
                   "ORDER BY s_id ")
            cursor.execute(sql)
            # connection.commit()
            result = cursor.fetchall()
    finally:
        connection.close()

    df = pd.DataFrame(result)
    print(df)

def f3():
    ### insert a new university ###
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27_project',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    u_name = input("University name: ")
    capacity = input("University capacity: ")
    group = input("University group: ")
    cutline = input("Cutline score: ")
    weight = input("Weight of high school records: ")

    try:
        with connection.cursor() as cursor:
            sql = ("INSERT INTO university "
                   "    VALUES(%s, %d, %s, %d, %.1f) ")
            cursor.execute(sql, u_name, capacity, group, cutline, weight)
            connection.commit()
            result = cursor.fetchall()
    finally:
        connection.close()

