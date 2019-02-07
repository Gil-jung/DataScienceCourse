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
            sql = ("SELECT university.*, count(apply.u_id) as applied "
                   "FROM university left outer join apply on (university.u_id = apply.u_id) "
                   "GROUP BY university.u_id, university.u_name, university.capacity, university.u_group, university.cutline, university.weight "
                   "ORDER BY university.u_id ")
            cursor.execute(sql)
            # connection.commit()
            result = cursor.fetchall()
            df = pd.DataFrame(result)
            df.sort_index(axis=1)
            print(df)
            print()
    except ValueError:
        print("There is no records. Please insert university record by press 3")
        print()
    finally:
        connection.close()
    print()


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
            df = pd.DataFrame(result)
            print(df)
            print()
    except ValueError:
        print("There is no records. Please insert student record by press 5")
        print()
    finally:
        connection.close()
    print()


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
    capacity = int(input("University capacity: "))
    group = input("University group: ")
    cutline = int(input("Cutline score: "))
    weight = float(input("Weight of high school records: "))

    try:
        with connection.cursor() as cursor:
            sql = ("INSERT INTO university(u_name, capacity, u_group, cutline, weight) "
                   "    VALUES(%s, %s, %s, %s, %s) ")
            cursor.execute(sql, (u_name, capacity, group, cutline, weight))
            connection.commit()
            # result = cursor.fetchall()
        print("A university is successfully inserted.")
        print()
    except ValueError:
        print("You insert wrong data. a university doesn't updated")
        print()
    finally:
        connection.close()


def f4():
    ### remove a university ###
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27_project',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    u_id = int(input("University ID: "))

    try:
        with connection.cursor() as cursor:
            sql1 = ("SELECT u_id " 
                    "FROM university "
                    "WHERE u_id = %s " )
            cursor.execute(sql1, u_id)
            result1 = cursor.fetchall()
            # print(result1[0]['u_id'])
            if result1[0]['u_id'] == u_id :
                sql = ("DELETE FROM university "
                       "       WHERE u_id = %s ")
                cursor.execute(sql, u_id)
                connection.commit()
        print("A university is successfully removed.")
        print()
    except IndexError:
        print("A university is not founded")
        print()
    finally:
        connection.close()


def f5():
    ### insert a new student ###
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27_project',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    s_name = input("Student name: ")
    csat_score = int(input("CSAT score: "))
    school_score = int(input("High school record score: "))

    try:
        with connection.cursor() as cursor:
            sql = ("INSERT INTO student(s_name, csat_score, school_score) "
                   "    VALUES(%s, %s, %s) ")
            cursor.execute(sql, (s_name, csat_score, school_score))
            connection.commit()
            # result = cursor.fetchall()
        print("A student is successfully inserted.")
        print()
    except ValueError:
        print("You insert wrong data. a student doesn't updated")
        print()
    finally:
        connection.close()


def f6():
    ### remove a student ###
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27_project',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    s_id = int(input("Student ID: "))

    try:
        with connection.cursor() as cursor:
            sql1 = ("SELECT s_id " 
                    "FROM student "
                    "WHERE s_id = %s " )
            cursor.execute(sql1, s_id)
            result1 = cursor.fetchall()
            # print(result1[0]['u_id'])
            if result1[0]['s_id'] == s_id :
                sql = ("DELETE FROM student "
                       "       WHERE s_id = %s ")
                cursor.execute(sql, s_id)
                connection.commit()
        print("A student is successfully removed.")
        print()
    except IndexError:
        print("A student is not founded")
        print()
    finally:
        connection.close()


def f7():
    ### make an application ###
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27_project',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    s_id = int(input("Student ID: "))
    u_id = int(input("University ID: "))

    try:
        with connection.cursor() as cursor:
            sql = ("INSERT INTO apply(s_id, u_id ) "
                   "    VALUES(%s, %s) ")
            cursor.execute(sql, (s_id, u_id))
            connection.commit()
            # result = cursor.fetchall()
        print("Successfully made an application.")
        print()
    # except ValueError:
    #     print("You insert wrong data. a student doesn't updated")
    #     print()
    finally:
        connection.close()