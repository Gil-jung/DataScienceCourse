from university_apply import *

if __name__ == "__main__":

    print("=============================================================")
    print("1. print all universities")
    print("2. print all students")
    print("3. insert a new university")
    print("4. remove a university")
    print("5. insert a new student")
    print("6. remove a student")
    print("7. make an application")
    print("8. print all students who applied for a university")
    print("9. print all universities a student applied for")
    print("10. print expected successful applicants of a university")
    print("11. print universities expected to accept a student")
    print("12. exit")
    print("13. reset database")
    print("=============================================================")

    option = 0
    while option != 12:
        option = int(input("Select your action: "))
        if option == 1:
             f1()
        elif option == 2:
             f2()
        elif option == 3:
             f3()
        elif option == 4:
             f4()
        elif option == 5:
             f5()
        elif option == 6:
             f6()
        elif option == 7:
             f7()
        elif option == 8:
             f8()
        elif option == 9:
             f9()
        elif option == 10:
             f10()
        elif option == 11:
             f11()
        elif option == 13:
             f13()

    print("Bye!")

