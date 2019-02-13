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
            result = cursor.fetchall()

    except ValueError:
        print("There is no records. Please insert university record by press 3")
        print()
    finally:
        connection.close()

    df = pd.DataFrame(result)
    cols_order = ['u_id', 'u_name', 'capacity', 'u_group', 'cutline', 'weight', 'applied']
    df = df[cols_order]
    newcols = {'u_id': 'id', 'u_name': 'name', 'u_group': 'group' }
    # df.sort_index(axis=1)
    print(df.rename(columns = newcols).to_string(index=False))
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
            result = cursor.fetchall()

    except ValueError:
        print("There is no records. Please insert student record by press 5")
        print()
    finally:
        connection.close()

    df = pd.DataFrame(result)
    cols_order = ['s_id', 's_name', 'csat_score', 'school_score']
    df = df[cols_order]
    newcols = {'s_id': 'id', 's_name': 'name'}
    # df.sort_index(axis=1)
    print(df.rename(columns = newcols).to_string(index=False))
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
            sql1 = ("INSERT INTO apply(s_id, u_id ) "
                   "    VALUES(%s, %s) ")
            sql2 = ("SELECT count(u_group) as count "
                    "FROM university natural join apply "
                    "WHERE s_id = %s and u_id = %s ")
            cursor.execute(sql1, (s_id, u_id))
            connection.commit()
            cursor.execute(sql2, (s_id, u_id))
            result = cursor.fetchall()
            # if result > 1:
            #     connection.rollback()
            #     print("This university group already applied")
            # else:
            #     print("Successfully made an application.")
            #     print()
    # except ValueError:
    #     print("You insert wrong data. a student doesn't updated")
    #     print()
    finally:
        connection.close()


def f8():
    ### print all students who applied for a university ###
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
            sql = ("SELECT * "
                   "FROM student natural join apply "
                   "WHERE u_id = %s "
                   "ORDER BY s_id ")
            cursor.execute(sql, u_id)
            result = cursor.fetchall()

    except ValueError:
        print("There is no university apply records. Please insert apply record by press 7")
        print()
    finally:
        connection.close()

    df = pd.DataFrame(result)
    cols_order = ['s_id', 's_name', 'csat_score', 'school_score']
    df = df[cols_order]
    newcols = {'s_id': 'id', 's_name': 'name'}
    # df.sort_index(axis=1)
    print(df.rename(columns = newcols).to_string(index=False))
    print()


def f9():
    ### print all universities a student applied for ###
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
            sql = ("SELECT university.*, count(apply.u_id) as applied "
                   "FROM university natural join apply "
                   "WHERE s_id = %s "
                   "GROUP BY university.u_id, university.u_name, university.capacity, university.u_group, university.cutline, university.weight "
                   "ORDER BY university.u_id ")
            cursor.execute(sql, s_id)
            result = cursor.fetchall()

    except ValueError:
        print("There is no student apply records. Please insert apply record by press 7")
        print()
    finally:
        connection.close()

    df = pd.DataFrame(result)
    cols_order = ['u_id', 'u_name', 'capacity', 'u_group', 'cutline', 'weight', 'applied']
    df = df[cols_order]
    newcols = {'u_id': 'id', 'u_name': 'name', 'u_group': 'group' }
    # df.sort_index(axis=1)
    print(df.rename(columns = newcols).to_string(index=False))
    print()


def f10():
    ### print expected successful applicants of a university ###
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
            sql = ("SELECT a.s_id, a.s_name, a.school_score, a.csat_score "
                   "FROM ( "
                   "	SELECT *, @curRank := @curRank + 1 as rank "
                   "	FROM university natural join apply "
                   "					natural join student, "
                   "		(SELECT @curRank := 0) r "
                   "	WHERE "
                   "		apply.u_id = %s and "
                   "		cutline <= csat_score + (school_score * weight) "
                   "	ORDER BY csat_score + (school_score * weight) desc ) a "
                   "WHERE rank <= capacity ")
            cursor.execute(sql, u_id)
            result = cursor.fetchall()

    except ValueError:
        print("There is no university apply records. Please insert apply record by press 7")
        print()
    finally:
        connection.close()

    df = pd.DataFrame(result)
    cols_order = ['s_id', 's_name', 'csat_score', 'school_score']
    df = df[cols_order]
    newcols = {'s_id': 'id', 's_name': 'name'}
    # df.sort_index(axis=1)
    print(df.rename(columns = newcols).to_string(index=False))
    print()


def f11():
    ### print universities expected to accept a student ###
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
            sql = ("SELECT a.u_id, a.u_name, a.capacity, a.u_group, a.cutline, a.weight, count(a.u_id) as applied "
                   "FROM ( "
                   "	SELECT *, @curRank := @curRank + 1 as rank "
                   "	FROM university natural join apply "
                   "					natural join student, "
                   "		(SELECT @curRank := 0) r "
                   "	WHERE "
                   "		apply.s_id = %s and "
                   "		cutline <= csat_score + (school_score * weight) "
                   "	ORDER BY csat_score + (school_score * weight) desc ) a "
                   "WHERE rank <= capacity "
                   "GROUP BY a.u_id, a.u_name, a.capacity, a.u_group, a.cutline, a.weight ")
            cursor.execute(sql, s_id)
            result = cursor.fetchall()

    except ValueError:
        print("There is no student apply records. Please insert apply record by press 7")
        print()
    finally:
        connection.close()

    df = pd.DataFrame(result)
    cols_order = ['u_id', 'u_name', 'capacity', 'u_group', 'cutline', 'weight', 'applied']
    df = df[cols_order]
    newcols = {'u_id': 'id', 'u_name': 'name', 'u_group': 'group' }
    # df.sort_index(axis=1)
    print(df.rename(columns = newcols).to_string(index=False))
    print()


def f13():
    ### reset database ###
    connection = pymysql.connect(
        host='ds4.snu.ac.kr',
        user='ds3_27',
        passwd='victory7&',
        db='ds3_27_project',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql1 = ("drop table if exists apply cascade; ")
            sql2 = ("drop table if exists student cascade; ")
            sql3 = ("drop table if exists university cascade; ")
            sql4 = ("create table university  "
                    "( "
                    "    u_id      		int  			not null auto_increment, "
                    "    u_name 		varchar(200), "
                    "    capacity    	int				check (capacity >= 1), "
                    "    u_group		char(1) 		check (u_group in ('A', 'B', 'C')), "
                    "    cutline		int				check (cutline >= 0), "
                    "    weight			numeric(1,1)	check (weight >= 0), "
                    "    primary key (u_id) "
                    "); ")
            sql5 = ("create table student "
                   "( "
                   "    s_id      		int  			not null auto_increment, "
                   "    s_name 			varchar(200), "
                   "    csat_score  	int				check (csat_score >= 0 and csat_score <= 400), "
                   "    school_score	int				check (school_score >= 0 and school_score <= 100), "
                   "    primary key (s_id) "
                   "); ")
            sql6 = ("create table apply "
                    "( "
                    "   s_id      		int  			not null, "
                    "   u_id			int				not null, "
                    "   foreign key (s_id) references student(s_id) "
                    "       on delete cascade, "
                    "   foreign key (u_id) references university(u_id) "
                    "       on delete cascade "
                    "); ")

            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
            cursor.execute(sql4)
            cursor.execute(sql5)
            cursor.execute(sql6)
            connection.commit()
            # result = cursor.fetchall()
            # df = pd.DataFrame(result)
            # print(df)
            # print()
            print("Successfully reset database.")
            print()
    except :
        print("There are some problems. couldn't applied")
        print()
    finally:
        connection.close()
    print()