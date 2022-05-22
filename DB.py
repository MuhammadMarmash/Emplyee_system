import sqlite3
import datetime


class DBConnect:
    def __init__(self):
        self._db = sqlite3.connect("The_employee_db.db")
        self._db.row_factory = sqlite3.Row
        # self._db.execute("""create table if not exists employers(employee_number integer,
        #  identification integer,
        #  Name text,
        #  StartDate text,
        #  EndDate text,
        #   employee_photo BLOP,
        #   Primary key(employee_number, identification, Name))""")
        # self._db.commit()

    def end_task(self, employee_number):
        time_now = str(datetime.datetime.now())
        time_now = str(datetime.date(int(time_now[:4]), int(time_now[5:7]), int(time_now[8:10])))
        self._db.execute("update employers set EndDate=? where employee_number=?", (time_now, employee_number))
        self._db.commit()

    def the_last_employee_id(self):
        cursor = self._db.execute("SELECT * FROM employers")
        last_employee_number = 0
        for row in cursor:
            if row["employee_number"] >= 1:
                last_employee_number = row["employee_number"]
        return last_employee_number + 1

    def add_employee(self, identification, name, employee_photo, dep, manager, phone, salary):
        time_now = str(datetime.datetime.now())
        time_now = str(datetime.date(int(time_now[:4]), int(time_now[5:7]), int(time_now[8:10])))
        self._db.execute("""insert into employers(
        identification,
        Name,
        StartDate,
        Department,
        Manager_Name,
        Phone_number,
        salary,
                employee_photo)
         values(?,?,?,?,?,?,?,?)""", (identification, name, time_now, dep, manager, phone, salary, employee_photo))
        self._db.commit()
        return "data is submitted"

    def start_day(self, employee_number):
        x = self._db.execute("select StartDate from employers where employee_number={}".format(employee_number))
        for row in x:
            y = row["StartDate"]
        return y

    def end_day(self, employee_number):
        x = self._db.execute("select EndDate from employers where employee_number={}".format(employee_number))
        for row in x:
            y = row["EndDate"]
        return y

    def change_manager(self, number, new_manager):
        self._db.execute("update employers set Manager_Name=? where employee_number=?", (new_manager, number))
        self._db.commit()

    def change_deportment(self, number, new_deportment):
        self._db.execute("update employers set Department=? where employee_number=?", (new_deportment, number))
        self._db.commit()

    def change_salary(self, number, new_salary):
        self._db.execute("update employers set salary=? where employee_number=?", (new_salary, number))
        self._db.commit()

    def employee_information(self):
        cursor = self._db.execute("select * from employers")
        return cursor

    def employee_name(self, identification):
        name = self._db.execute("SELECT * FROM employers WHERE employee_number={}".format(identification))
        return name

    def search_by_identification(self, identification):
        employee_information = self._db.execute("select * from employers where identification={}"
                                                .format(identification))
        return employee_information

    def search_by_employee_number(self, employee_number):
        employee_information = self._db.execute("select * from employers where employee_number={}"
                                                .format(employee_number))
        return employee_information

    def identification_check(self, new_id):
        cursor = self._db.execute("SELECT * FROM employers")
        available_check = False
        for row in cursor:
            if row["identification"] == int(new_id):
                available_check = True
                break
        return available_check

    def name_check(self, new_name):
        cursor = self._db.execute("SELECT * FROM employers")
        available_check = False
        for row in cursor:
            if row["Name"] == new_name:
                available_check = True
                break
        return available_check

    def search_by_name(self, name):
        employee_information = self._db.execute("select * from employers where Name={}"
                                                .format(name))
        return employee_information

    def delete_employee(self, identification):
        self._db.execute("delete from employers where employee_number={}".format(identification))
        self._db.commit()
        return "your employee data has been removed"

    # def update_password(self, identification, new_password):
    #     self._db.execute("update employers set Password=? where employee_number=?", (new_password, identification))
    #     self._db.commit()
    #     return "your password has been updated

    def get_deparment(self):
        return self._db.execute("select * from Department")

    def search_department(self, id):
        return self._db.execute("select * from Department where Dep_id={}".format(id))

    def add_deparment(self, name, manager):
        self._db.execute("insert into Department(Dep_Name,Manager) values(?,?)", (name, manager))
        self._db.commit()

    def change_manager_dep(self, id, new_manager):
        self._db.execute("update Department set Manager=? where Dep_id=?", (new_manager, id))
        self._db.commit()

    def delete_deb(self, id):
        self._db.execute("delete from Department where Dep_id={}".format(id))
        self._db.commit()
