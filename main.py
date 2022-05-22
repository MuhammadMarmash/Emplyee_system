from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB import DBConnect
from PIL import ImageTk, Image
from tkinter import filedialog
from tkscrolledframe import ScrolledFrame
import pyautogui


def app():
    # connect do database
    db = DBConnect()

    # style the main window
    main_window = Tk()
    main_window.iconphoto(False, ImageTk.PhotoImage(Image.open(""
                                                               "m"
                                                               "a"
                                                               "n"
                                                               "-"
                                                               "l"
                                                               "o"
                                                               "o"
                                                               "k"
                                                               "-"
                                                               "g"
                                                               "r"
                                                               "a"
                                                               "p"
                                                               "h"
                                                               "i"
                                                               "c"
                                                               "-"
                                                               "c"
                                                               "h"
                                                               "a"
                                                               "r"
                                                               "t"
                                                               "-"
                                                               "b"
                                                               "u"
                                                               "s"
                                                               "i"
                                                               "n"
                                                               "e"
                                                               "s"
                                                               "s"
                                                               "-"
                                                               "a"
                                                               "n"
                                                               "a"
                                                               "l"
                                                               "y"
                                                               "t"
                                                               "i"
                                                               "c"
                                                               "s"
                                                               "-"
                                                               "c"
                                                               "o"
                                                               "n"
                                                               "c"
                                                               "e"
                                                               "p"
                                                               "t"
                                                               "-"
                                                               "b"
                                                               "i"
                                                               "g"
                                                               "-"
                                                               "d"
                                                               "a"
                                                               "t"
                                                               "a"
                                                               "-"
                                                               "p"
                                                               "r"
                                                               "o"
                                                               "c"
                                                               "e"
                                                               "s"
                                                               "s"
                                                               "i"
                                                               "n"
                                                               "g"
                                                               "-"
                                                               "i"
                                                               "c"
                                                               "o"
                                                               "n"
                                                               "_"
                                                               "3"
                                                               "9"
                                                               "4"
                                                               "2"
                                                               "2"
                                                               "-"
                                                               "7"
                                                               "6"
                                                               "1"
                                                               " "
                                                               "("
                                                               "1"
                                                               ")"
                                                               "."
                                                               "p"
                                                               "n"
                                                               "g"
                                                               "")))
    main_window.title("EMPLOYEE SYSTEM")
    main_style = ttk.Style()
    main_style.theme_use("classic")
    main_window.configure(background='#e1d8b2')
    main_style.configure('TLabel', background='#e1d8b2')
    main_style.configure('TButton', background='#e1d8b2')
    main_style.configure('TRadiobutton', background='#e1d8b2')
    main_style.configure('TLabelframe', background='#e1d8b2')

    # design search form
    search_lapel = ttk.Label(main_window, text="search employee: ").grid(row=0, column=0, sticky="snew")
    search_entry = ttk.Entry(main_window)
    search_entry.grid(row=0, column=1)

    def has_numbers(string_):
        number_of_numbers = 0
        for char in string_:
            if char.isnumeric():
                number_of_numbers += 1
        return number_of_numbers

    def search():
        search_e = search_entry.get()
        search_entry.delete(0, END)
        if search_e == "":
            messagebox.showinfo(title="ERROR", message="you can't search of nothing")
        else:
            if "dep" in search_e:
                search_e = search_e[:-3]
                employee = db.search_department(search_e)

                sf = ScrolledFrame(main_window)
                sf.grid(row=1, column=0)

                # Bind the arrow keys and scroll wheel
                sf.bind_arrow_keys(main_window)
                sf.bind_scroll_wheel(main_window)

                # Create a frame within the ScrolledFrame
                inner_frame = sf.display_widget(Frame)

                employee_frame = ttk.LabelFrame(inner_frame, text="employee information")
                employee_frame.grid(row=1, column=0)
                try:
                    for row in employee:
                        dep_id = row["Dep_id"]
                        dep_name = row["Dep_Name"]
                        manager = row["Manager"]
                    dep_idd = ttk.Label(employee_frame, text=f"department id:").grid(row=0,
                                                                                     column=0,
                                                                                     columnspan=2,
                                                                                     sticky="snew",
                                                                                     padx=50)
                    dep_namee = ttk.Label(employee_frame, text=f"department name:").grid(row=0,
                                                                                         column=2,
                                                                                         columnspan=2,
                                                                                         sticky="snew",
                                                                                         padx=50)
                    dep_manager = ttk.Label(employee_frame, text=f"manager:").grid(row=0,
                                                                                   column=4,
                                                                                   columnspan=2,
                                                                                   sticky="snew",
                                                                                   padx=50)
                    # employee_start_date = ttk.Label(employee_frame, text=f"Start Date:").grid(row=0, column=6, columnspan=2,
                    #                                                                           sticky="snew", padx=50)
                    # employee_end_date = ttk.Label(employee_frame, text=f"End Date:").grid(row=0, column=8, columnspan=2,
                    #                                                                       sticky="snew", padx=50)
                    # dep_label = ttk.Label(employee_frame, text=f"Deportment:").grid(row=0, column=10, columnspan=2,
                    #                                                                 sticky="snew", padx=50)
                    # manager_lapel = ttk.Label(employee_frame, text=f"Manager:").grid(row=0, column=12, columnspan=2,
                    #                                                                  sticky="snew", padx=50)
                    # phone_number = ttk.Label(employee_frame, text=f"Phone number:").grid(row=0, column=14, columnspan=2,
                    #                                                                      sticky="snew", padx=50)
                    # phone_number = ttk.Label(employee_frame, text=f"salary:").grid(row=0, column=16, columnspan=2,
                    #                                                                sticky="snew", padx=50)
                    # employee_photo = ttk.Label(employee_frame, text="photo:").grid(row=0, column=18, columnspan=2,
                    #                                                                sticky="snew", padx=50)
                    # employee_number = ttk.Label(employee_frame, text=f"{employee_numberrr}").grid(row=1, column=0,
                    #                                                                               columnspan=2,
                    #                                                                               sticky="snew",
                    #                                                                               padx=50)
                    # employee_name = ttk.Label(employee_frame, text=f"{name}").grid(row=1, column=2, columnspan=2,
                    #                                                                sticky="snew", padx=50)
                    # employee_identification = ttk.Label(employee_frame, text=f"{id1}").grid(row=1, column=4,
                    #                                                                         columnspan=2, sticky="snew",
                    #                                                                         padx=50)
                    # employee_start = ttk.Label(employee_frame, text=f"{start_date}").grid(row=1, column=6,
                    #                                                                       columnspan=2, sticky="snew", padx=50)
                    # employee_end = ttk.Label(employee_frame, text=f"{end_date}").grid(row=1, column=8, columnspan=2,
                    #                                                                   sticky="snew", padx=50)
                    # dep_label = ttk.Label(employee_frame, text=f"{deportment}").grid(row=1, column=10, columnspan=2,
                    #                                                                  sticky="snew", padx=50)
                    id_la = ttk.Label(employee_frame, text=f"{dep_id}").grid(row=1,
                                                                             column=0,
                                                                             columnspan=2,
                                                                             sticky="snew",
                                                                             padx=50)
                    na_la = ttk.Label(employee_frame, text=f"{dep_name}").grid(row=1,
                                                                               column=2,
                                                                               columnspan=2,
                                                                               sticky="snew",
                                                                               padx=50)
                    ma_la = ttk.Label(employee_frame, text=f"{manager}").grid(row=1,
                                                                              column=4,
                                                                              columnspan=2,
                                                                              sticky="snew",
                                                                              padx=50)

                    manager_choice_variable = StringVar()
                    managers = ["", ]
                    for row in db.employee_information():
                        managers.append(row["Name"])
                    managers_choice = ttk.OptionMenu(employee_frame, manager_choice_variable, *managers)
                    managers_choice.grid(row=2, column=4, columnspan=2)

                    def change_manager():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.change_manager_dep(search_e, manager_choice_variable.get())
                            messagebox.showinfo(title="DONE", message="data is submitted")

                    managers_choice_bu = ttk.Button(employee_frame,
                                                    text="change department manager",
                                                    command=change_manager)
                    managers_choice_bu.grid(row=3, column=4, columnspan=2)

                    def delete_deb():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.delete_deb(search_e)
                            messagebox.showinfo(title="DONE", message=f"department {search_e} is deleted")

                    delete_bu = ttk.Button(employee_frame,
                                                    text="delete department",
                                                    command=delete_deb)
                    delete_bu.grid(row=3, column=0)
                except Exception:
                    messagebox.showinfo(title="ERROR", message="there is no department with this id")
                #     photo_photo = ImageTk.PhotoImage(Image.open("employee_photo.png"))
                #     employee_photo1 = Label(employee_frame, image=photo_photo)
                #     employee_photo1.image = photo_photo
                #     employee_photo1.grid(row=1, column=18, columnspan=2, sticky="snew", padx=50)
                #
                #     new_salary_entry = ttk.Entry(employee_frame)
                #     new_salary_entry.grid(row=2, column=16)
                #     def change_salary():
                #         new = new_salary_entry.get()
                #         new_check = False
                #         if new == "":
                #             new_check = True
                #         else:
                #             for num in str(new):
                #                 if not num.isnumeric():
                #                     new_check = True
                #                     break
                #                 else:
                #                     new_check = False
                #         if not new_check:
                #             db.change_salary(int(search_e), int(new))
                #         else:
                #             pass
                #     change_bu = ttk.Button(employee_frame, text="change salary", command=change_salary)
                #     change_bu.grid(row=3, column=16)
                #
                #     new_manager = StringVar()
                #     managers = ["", ]
                #     for row in db.employee_information():
                #         managers.append(row["Name"])
                #     managers_choice = ttk.OptionMenu(employee_frame, new_manager, *managers)
                #     managers_choice.grid(row=2, column=12)
                #     def change_maneger():
                #         sure = messagebox.askquestion("hi", "Are you sure")
                #         if sure == "yes":
                #             db.change_manager(search_e, new_manager.get())
                #         else:
                #             pass
                #     change_bu = ttk.Button(employee_frame, text="change manager", command=change_maneger)
                #     change_bu.grid(row=3, column=12, sticky="snew")
                #     debarment_choice_variable = StringVar()
                #     debarments = [""]
                #     for row in db.get_deparment():
                #         debarments.append(row["Dep_Name"])
                #     debarment_choice = ttk.OptionMenu(employee_frame, debarment_choice_variable, *debarments)
                #     debarment_choice.grid(row=2, column=10, stick="snew")
                #     def change_dep():
                #         sure = messagebox.askquestion("hi", "Are you sure")
                #         if sure == "yes":
                #             db.change_manager(search_e, debarment_choice_variable.get())
                #         else:
                #             pass
                #     change_bu = ttk.Button(employee_frame, text="change department", command=change_dep)
                #     change_bu.grid(row=3, column=10, sticky="snew")
                #     def end_task():
                #         db.end_task(search_e)
                #         messagebox.showinfo(title="BY BY", message=f"{name} IS ENDED TASK")
                #     if not (db.end_day(search_e) is None):
                #         pass
                #     else:
                #         end_task_bu = ttk.Button(employee_frame, text="END TASK", command=end_task)
                #         end_task_bu.grid(row=2, column=8, sticky="snew")
                #     def delete_employee():
                #         sure = messagebox.askquestion("hi", "Are you sure")
                #         if sure == "yes":
                #             id = search_e
                #             if id == "":
                #                 messagebox.showinfo(title="ERROR", message="you can't delete me")
                #             else:
                #                 x = db.employee_name(id)
                #                 for row in x:
                #                     try:
                #                         db.delete_employee(id)
                #                         messagebox.showinfo(title="DONE", message=f"{row['Name']} has been removed")
                #                     except Exception:
                #                         print(row['Name'])
                #                         messagebox.showinfo(title="ERROR", message=f"there is no one have this number{id}")
                #     delete_bu = ttk.Button(employee_frame, text="Delete", command=delete_employee)
                #     delete_bu.grid(row=2, column=0, sticky="snew")
                # except Exception:
                #     messagebox.showinfo(title="ERROR", message=f"there is no employee with this id({search_e})")

            else:
                employee = db.search_by_employee_number(search_e)
                sf = ScrolledFrame(main_window, width=640, height=480)
                sf.grid(sticky="snew", row=1, column=0, columnspan=7)

                # Bind the arrow keys and scroll wheel
                sf.bind_arrow_keys(main_window)
                sf.bind_scroll_wheel(main_window)

                # Create a frame within the ScrolledFrame
                inner_frame = sf.display_widget(Frame)

                employee_frame = ttk.LabelFrame(inner_frame, text="employee information")
                employee_frame.grid(row=1, column=0, columnspan=5, sticky="snew")
                try:
                    for row in employee:
                        employee_numberrr = row['employee_number']
                        name = row['Name']
                        id1 = row['identification']
                        start_date = row['StartDate']
                        end_date = row['EndDate']
                        deportment = row['Department']
                        maneger_name = row['Manager_Name']
                        phone_number1 = row['Phone_number']
                        salary = row['salary']
                        photo = row['employee_photo']
                    photo_write = open("employee_photo.png", "wb")
                    photo_write.write(photo)
                    photo_write.close()
                    employee_number = ttk.Label(employee_frame, text=f"employee number:").grid(row=0, column=0, columnspan=2,
                                                                                               sticky="snew", padx=50)
                    employee_name = ttk.Label(employee_frame, text=f"name:").grid(row=0, column=2, columnspan=2, sticky="snew",
                                                                                  padx=50)
                    employee_identification = ttk.Label(employee_frame, text=f"id:").grid(row=0, column=4, columnspan=2,
                                                                                          sticky="snew", padx=50)
                    employee_start_date = ttk.Label(employee_frame, text=f"Start Date:").grid(row=0, column=6, columnspan=2,
                                                                                              sticky="snew", padx=50)
                    employee_end_date = ttk.Label(employee_frame, text=f"End Date:").grid(row=0, column=8, columnspan=2,
                                                                                          sticky="snew", padx=50)
                    dep_label = ttk.Label(employee_frame, text=f"Deportment:").grid(row=0, column=10, columnspan=2,
                                                                                    sticky="snew", padx=50)
                    manager_lapel = ttk.Label(employee_frame, text=f"Manager:").grid(row=0, column=12, columnspan=2,
                                                                                     sticky="snew", padx=50)
                    phone_number = ttk.Label(employee_frame, text=f"Phone number:").grid(row=0, column=14, columnspan=2,
                                                                                         sticky="snew", padx=50)
                    phone_number = ttk.Label(employee_frame, text=f"salary:").grid(row=0, column=16, columnspan=2,
                                                                                   sticky="snew", padx=50)
                    employee_photo = ttk.Label(employee_frame, text="photo:").grid(row=0, column=18, columnspan=2,
                                                                                   sticky="snew", padx=50)
                    employee_number = ttk.Label(employee_frame, text=f"{employee_numberrr}").grid(row=1, column=0,
                                                                                                  columnspan=2,
                                                                                                  sticky="snew",
                                                                                                  padx=50)
                    employee_name = ttk.Label(employee_frame, text=f"{name}").grid(row=1, column=2, columnspan=2,
                                                                                   sticky="snew", padx=50)
                    employee_identification = ttk.Label(employee_frame, text=f"{id1}").grid(row=1, column=4,
                                                                                            columnspan=2, sticky="snew",
                                                                                            padx=50)
                    employee_start = ttk.Label(employee_frame, text=f"{start_date}").grid(row=1, column=6,
                                                                                          columnspan=2, sticky="snew", padx=50)
                    employee_end = ttk.Label(employee_frame, text=f"{end_date}").grid(row=1, column=8, columnspan=2,
                                                                                      sticky="snew", padx=50)
                    dep_label = ttk.Label(employee_frame, text=f"{deportment}").grid(row=1, column=10, columnspan=2,
                                                                                     sticky="snew", padx=50)
                    manager_lapel = ttk.Label(employee_frame, text=f"{maneger_name}").grid(row=1, column=12, columnspan=2,
                                                                                           sticky="snew", padx=50)
                    phone_number = ttk.Label(employee_frame, text=f"{phone_number1}").grid(row=1, column=14, columnspan=2,
                                                                                           sticky="snew", padx=50)
                    salary1 = ttk.Label(employee_frame, text=f"{salary}").grid(row=1, column=16, columnspan=2,
                                                                               sticky="snew", padx=50)
                    # employee_password = ttk.Label(employee_frame, text=f"{password}").grid(row=1,
                    # column=4, columnspan=2, sticky="snew", padx=50)
                    photo_photo = ImageTk.PhotoImage(Image.open("employee_photo.png"))
                    employee_photo1 = Label(employee_frame, image=photo_photo)
                    employee_photo1.image = photo_photo
                    employee_photo1.grid(row=1, column=18, columnspan=2, sticky="snew", padx=50)

                    new_salary_entry = ttk.Entry(employee_frame)
                    new_salary_entry.grid(row=2, column=16)

                    def change_salary():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            new = new_salary_entry.get()
                            new_check = False
                            if new == "":
                                new_check = True
                            else:
                                for num in str(new):
                                    if not num.isnumeric():
                                        new_check = True
                                        break
                                    else:
                                        new_check = False
                        else:
                            pass

                        if not new_check:
                            db.change_salary(int(search_e), int(new))
                        else:
                            pass

                    change_bu = ttk.Button(employee_frame, text="change salary", command=change_salary)
                    change_bu.grid(row=3, column=16)

                    new_manager = StringVar()
                    managers = ["", ]
                    for row in db.employee_information():
                        managers.append(row["Name"])
                    managers_choice = ttk.OptionMenu(employee_frame, new_manager, *managers)
                    managers_choice.grid(row=2, column=12)

                    def change_maneger():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.change_manager(search_e, new_manager.get())
                        else:
                            pass

                    change_bu = ttk.Button(employee_frame, text="change manager", command=change_maneger)
                    change_bu.grid(row=3, column=12, sticky="snew")

                    debarment_choice_variable = StringVar()
                    debarments = [""]
                    for row in db.get_deparment():
                        debarments.append(row["Dep_Name"])
                    debarment_choice = ttk.OptionMenu(employee_frame, debarment_choice_variable, *debarments)
                    debarment_choice.grid(row=2, column=10, stick="snew")

                    def change_dep():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.change_manager(search_e, debarment_choice_variable.get())
                        else:
                            pass

                    change_bu = ttk.Button(employee_frame, text="change department", command=change_dep)
                    change_bu.grid(row=3, column=10, sticky="snew")

                    def end_task():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.end_task(search_e)
                            messagebox.showinfo(title="BY BY", message=f"{name} IS ENDED TASK")
                        else:
                            pass

                    if not (db.end_day(search_e) is None):
                        pass
                    else:
                        end_task_bu = ttk.Button(employee_frame, text="END TASK", command=end_task)
                        end_task_bu.grid(row=2, column=8, sticky="snew")

                    def delete_employee():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            id = search_e
                            if id == "":
                                messagebox.showinfo(title="ERROR", message="you can't delete me")
                            else:
                                x = db.employee_name(id)
                                for row in x:
                                    try:
                                        db.delete_employee(id)
                                        messagebox.showinfo(title="DONE", message=f"{row['Name']} has been removed")
                                    except Exception:
                                        print(row['Name'])
                                        messagebox.showinfo(title="ERROR", message=f"there is no one have this number{id}")

                    delete_bu = ttk.Button(employee_frame, text="Delete", command=delete_employee)
                    delete_bu.grid(row=2, column=0, sticky="snew")
                except Exception:
                    messagebox.showinfo(title="ERROR", message=f"there is no employee with this id({search_e})")

    def search_bind(event):
        search_e = search_entry.get()
        search_entry.delete(0, END)
        if search_e == "":
            messagebox.showinfo(title="ERROR", message="you can't search of nothing")
        else:
            if "dep" in search_e:
                search_e = search_e[:-3]
                employee = db.search_department(search_e)

                sf = ScrolledFrame(main_window)
                sf.grid(row=1, column=0)

                # Bind the arrow keys and scroll wheel
                sf.bind_arrow_keys(main_window)
                sf.bind_scroll_wheel(main_window)

                # Create a frame within the ScrolledFrame
                inner_frame = sf.display_widget(Frame)

                employee_frame = ttk.LabelFrame(inner_frame, text="employee information")
                employee_frame.grid(row=1, column=0)
                try:
                    for row in employee:
                        dep_id = row["Dep_id"]
                        dep_name = row["Dep_Name"]
                        manager = row["Manager"]
                    dep_idd = ttk.Label(employee_frame, text=f"department id:").grid(row=0,
                                                                                     column=0,
                                                                                     columnspan=2,
                                                                                     sticky="snew",
                                                                                     padx=50)
                    dep_namee = ttk.Label(employee_frame, text=f"department name:").grid(row=0,
                                                                                         column=2,
                                                                                         columnspan=2,
                                                                                         sticky="snew",
                                                                                         padx=50)
                    dep_manager = ttk.Label(employee_frame, text=f"manager:").grid(row=0,
                                                                                   column=4,
                                                                                   columnspan=2,
                                                                                   sticky="snew",
                                                                                   padx=50)
                    # employee_start_date = ttk.Label(employee_frame, text=f"Start Date:").grid(row=0, column=6, columnspan=2,
                    #                                                                           sticky="snew", padx=50)
                    # employee_end_date = ttk.Label(employee_frame, text=f"End Date:").grid(row=0, column=8, columnspan=2,
                    #                                                                       sticky="snew", padx=50)
                    # dep_label = ttk.Label(employee_frame, text=f"Deportment:").grid(row=0, column=10, columnspan=2,
                    #                                                                 sticky="snew", padx=50)
                    # manager_lapel = ttk.Label(employee_frame, text=f"Manager:").grid(row=0, column=12, columnspan=2,
                    #                                                                  sticky="snew", padx=50)
                    # phone_number = ttk.Label(employee_frame, text=f"Phone number:").grid(row=0, column=14, columnspan=2,
                    #                                                                      sticky="snew", padx=50)
                    # phone_number = ttk.Label(employee_frame, text=f"salary:").grid(row=0, column=16, columnspan=2,
                    #                                                                sticky="snew", padx=50)
                    # employee_photo = ttk.Label(employee_frame, text="photo:").grid(row=0, column=18, columnspan=2,
                    #                                                                sticky="snew", padx=50)
                    # employee_number = ttk.Label(employee_frame, text=f"{employee_numberrr}").grid(row=1, column=0,
                    #                                                                               columnspan=2,
                    #                                                                               sticky="snew",
                    #                                                                               padx=50)
                    # employee_name = ttk.Label(employee_frame, text=f"{name}").grid(row=1, column=2, columnspan=2,
                    #                                                                sticky="snew", padx=50)
                    # employee_identification = ttk.Label(employee_frame, text=f"{id1}").grid(row=1, column=4,
                    #                                                                         columnspan=2, sticky="snew",
                    #                                                                         padx=50)
                    # employee_start = ttk.Label(employee_frame, text=f"{start_date}").grid(row=1, column=6,
                    #                                                                       columnspan=2, sticky="snew", padx=50)
                    # employee_end = ttk.Label(employee_frame, text=f"{end_date}").grid(row=1, column=8, columnspan=2,
                    #                                                                   sticky="snew", padx=50)
                    # dep_label = ttk.Label(employee_frame, text=f"{deportment}").grid(row=1, column=10, columnspan=2,
                    #                                                                  sticky="snew", padx=50)
                    id_la = ttk.Label(employee_frame, text=f"{dep_id}").grid(row=1,
                                                                             column=0,
                                                                             columnspan=2,
                                                                             sticky="snew",
                                                                             padx=50)
                    na_la = ttk.Label(employee_frame, text=f"{dep_name}").grid(row=1,
                                                                               column=2,
                                                                               columnspan=2,
                                                                               sticky="snew",
                                                                               padx=50)
                    ma_la = ttk.Label(employee_frame, text=f"{manager}").grid(row=1,
                                                                              column=4,
                                                                              columnspan=2,
                                                                              sticky="snew",
                                                                              padx=50)

                    manager_choice_variable = StringVar()
                    managers = ["", ]
                    for row in db.employee_information():
                        managers.append(row["Name"])
                    managers_choice = ttk.OptionMenu(employee_frame, manager_choice_variable, *managers)
                    managers_choice.grid(row=2, column=4, columnspan=2)

                    def change_manager():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.change_manager_dep(search_e, manager_choice_variable.get())
                            messagebox.showinfo(title="DONE", message="data is submitted")

                    managers_choice_bu = ttk.Button(employee_frame,
                                                    text="change department manager",
                                                    command=change_manager)
                    managers_choice_bu.grid(row=3, column=4, columnspan=2)

                    def delete_deb():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.delete_deb(search_e)
                            messagebox.showinfo(title="DONE", message=f"department {search_e} is deleted")

                    delete_bu = ttk.Button(employee_frame,
                                           text="delete department",
                                           command=delete_deb)
                    delete_bu.grid(row=3, column=0)
                except Exception:
                    messagebox.showinfo(title="ERROR", message="there is no department with this id")
                #     photo_photo = ImageTk.PhotoImage(Image.open("employee_photo.png"))
                #     employee_photo1 = Label(employee_frame, image=photo_photo)
                #     employee_photo1.image = photo_photo
                #     employee_photo1.grid(row=1, column=18, columnspan=2, sticky="snew", padx=50)
                #
                #     new_salary_entry = ttk.Entry(employee_frame)
                #     new_salary_entry.grid(row=2, column=16)
                #     def change_salary():
                #         new = new_salary_entry.get()
                #         new_check = False
                #         if new == "":
                #             new_check = True
                #         else:
                #             for num in str(new):
                #                 if not num.isnumeric():
                #                     new_check = True
                #                     break
                #                 else:
                #                     new_check = False
                #         if not new_check:
                #             db.change_salary(int(search_e), int(new))
                #         else:
                #             pass
                #     change_bu = ttk.Button(employee_frame, text="change salary", command=change_salary)
                #     change_bu.grid(row=3, column=16)
                #
                #     new_manager = StringVar()
                #     managers = ["", ]
                #     for row in db.employee_information():
                #         managers.append(row["Name"])
                #     managers_choice = ttk.OptionMenu(employee_frame, new_manager, *managers)
                #     managers_choice.grid(row=2, column=12)
                #     def change_maneger():
                #         sure = messagebox.askquestion("hi", "Are you sure")
                #         if sure == "yes":
                #             db.change_manager(search_e, new_manager.get())
                #         else:
                #             pass
                #     change_bu = ttk.Button(employee_frame, text="change manager", command=change_maneger)
                #     change_bu.grid(row=3, column=12, sticky="snew")
                #     debarment_choice_variable = StringVar()
                #     debarments = [""]
                #     for row in db.get_deparment():
                #         debarments.append(row["Dep_Name"])
                #     debarment_choice = ttk.OptionMenu(employee_frame, debarment_choice_variable, *debarments)
                #     debarment_choice.grid(row=2, column=10, stick="snew")
                #     def change_dep():
                #         sure = messagebox.askquestion("hi", "Are you sure")
                #         if sure == "yes":
                #             db.change_manager(search_e, debarment_choice_variable.get())
                #         else:
                #             pass
                #     change_bu = ttk.Button(employee_frame, text="change department", command=change_dep)
                #     change_bu.grid(row=3, column=10, sticky="snew")
                #     def end_task():
                #         db.end_task(search_e)
                #         messagebox.showinfo(title="BY BY", message=f"{name} IS ENDED TASK")
                #     if not (db.end_day(search_e) is None):
                #         pass
                #     else:
                #         end_task_bu = ttk.Button(employee_frame, text="END TASK", command=end_task)
                #         end_task_bu.grid(row=2, column=8, sticky="snew")
                #     def delete_employee():
                #         sure = messagebox.askquestion("hi", "Are you sure")
                #         if sure == "yes":
                #             id = search_e
                #             if id == "":
                #                 messagebox.showinfo(title="ERROR", message="you can't delete me")
                #             else:
                #                 x = db.employee_name(id)
                #                 for row in x:
                #                     try:
                #                         db.delete_employee(id)
                #                         messagebox.showinfo(title="DONE", message=f"{row['Name']} has been removed")
                #                     except Exception:
                #                         print(row['Name'])
                #                         messagebox.showinfo(title="ERROR", message=f"there is no one have this number{id}")
                #     delete_bu = ttk.Button(employee_frame, text="Delete", command=delete_employee)
                #     delete_bu.grid(row=2, column=0, sticky="snew")
                # except Exception:
                #     messagebox.showinfo(title="ERROR", message=f"there is no employee with this id({search_e})")

            else:
                employee = db.search_by_employee_number(search_e)

                sf = ScrolledFrame(main_window, width=640, height=480)
                sf.grid(sticky="snew", row=1, column=0, columnspan=7)

                # Bind the arrow keys and scroll wheel
                sf.bind_arrow_keys(main_window)
                sf.bind_scroll_wheel(main_window)

                # Create a frame within the ScrolledFrame
                inner_frame = sf.display_widget(Frame)

                employee_frame = ttk.LabelFrame(inner_frame, text="employee information")
                employee_frame.grid(row=1, column=0, columnspan=5, sticky="snew")
                try:
                    for row in employee:
                        employee_numberrr = row['employee_number']
                        name = row['Name']
                        id1 = row['identification']
                        start_date = row['StartDate']
                        end_date = row['EndDate']
                        deportment = row['Deportment']
                        maneger_name = row['Manager_Name']
                        phone_number1 = row['Phone_number']
                        salary = row['salary']
                        photo = row['employee_photo']
                    photo_write = open("employee_photo.png", "wb")
                    photo_write.write(photo)
                    photo_write.close()
                    employee_number = ttk.Label(employee_frame, text=f"employee number:").grid(row=0, column=0,
                                                                                               columnspan=2,
                                                                                               sticky="snew", padx=50)
                    employee_name = ttk.Label(employee_frame, text=f"name:").grid(row=0, column=2, columnspan=2,
                                                                                  sticky="snew",
                                                                                  padx=50)
                    employee_identification = ttk.Label(employee_frame, text=f"id:").grid(row=0, column=4, columnspan=2,
                                                                                          sticky="snew", padx=50)
                    employee_start_date = ttk.Label(employee_frame, text=f"Start Date:").grid(row=0, column=6,
                                                                                              columnspan=2,
                                                                                              sticky="snew", padx=50)
                    employee_end_date = ttk.Label(employee_frame, text=f"End Date:").grid(row=0, column=8, columnspan=2,
                                                                                          sticky="snew", padx=50)
                    dep_label = ttk.Label(employee_frame, text=f"Deportment:").grid(row=0, column=10, columnspan=2,
                                                                                    sticky="snew", padx=50)
                    manager_lapel = ttk.Label(employee_frame, text=f"Manager:").grid(row=0, column=12, columnspan=2,
                                                                                     sticky="snew", padx=50)
                    phone_number = ttk.Label(employee_frame, text=f"Phone number:").grid(row=0, column=14, columnspan=2,
                                                                                         sticky="snew", padx=50)
                    phone_number = ttk.Label(employee_frame, text=f"salary:").grid(row=0, column=16, columnspan=2,
                                                                                   sticky="snew", padx=50)
                    employee_photo = ttk.Label(employee_frame, text="photo:").grid(row=0, column=18, columnspan=2,
                                                                                   sticky="snew", padx=50)
                    employee_number = ttk.Label(employee_frame, text=f"{employee_numberrr}").grid(row=1, column=0,
                                                                                                  columnspan=2,
                                                                                                  sticky="snew",
                                                                                                  padx=50)
                    employee_name = ttk.Label(employee_frame, text=f"{name}").grid(row=1, column=2, columnspan=2,
                                                                                   sticky="snew", padx=50)
                    employee_identification = ttk.Label(employee_frame, text=f"{id1}").grid(row=1, column=4,
                                                                                            columnspan=2, sticky="snew",
                                                                                            padx=50)
                    employee_start = ttk.Label(employee_frame, text=f"{start_date}").grid(row=1, column=6,
                                                                                          columnspan=2, sticky="snew",
                                                                                          padx=50)
                    employee_end = ttk.Label(employee_frame, text=f"{end_date}").grid(row=1, column=8, columnspan=2,
                                                                                      sticky="snew", padx=50)
                    dep_label = ttk.Label(employee_frame, text=f"{deportment}").grid(row=1, column=10, columnspan=2,
                                                                                     sticky="snew", padx=50)
                    manager_lapel = ttk.Label(employee_frame, text=f"{maneger_name}").grid(row=1, column=12,
                                                                                           columnspan=2,
                                                                                           sticky="snew", padx=50)
                    phone_number = ttk.Label(employee_frame, text=f"{phone_number1}").grid(row=1, column=14,
                                                                                           columnspan=2,
                                                                                           sticky="snew", padx=50)
                    salary1 = ttk.Label(employee_frame, text=f"{salary}").grid(row=1, column=16, columnspan=2,
                                                                               sticky="snew", padx=50)
                    # employee_password = ttk.Label(employee_frame, text=f"{password}").grid(row=1,
                    # column=4, columnspan=2, sticky="snew", padx=50)
                    photo_photo = ImageTk.PhotoImage(Image.open("employee_photo.png"))
                    employee_photo1 = Label(employee_frame, image=photo_photo)
                    employee_photo1.image = photo_photo
                    employee_photo1.grid(row=1, column=18, columnspan=2, sticky="snew", padx=50)

                    new_salary_entry = ttk.Entry(employee_frame)
                    new_salary_entry.grid(row=2, column=16)

                    def change_salary():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            new = new_salary_entry.get()
                            new_check = False
                            if new == "":
                                new_check = True
                            else:
                                for num in str(new):
                                    if not num.isnumeric():
                                        new_check = True
                                        break
                                    else:
                                        new_check = False
                        else:
                            pass

                        if not new_check:
                            db.change_salary(int(search_e), int(new))
                        else:
                            pass

                    change_bu = ttk.Button(employee_frame, text="change salary", command=change_salary)
                    change_bu.grid(row=3, column=16)

                    new_manager = StringVar()
                    managers = ["", ]
                    for row in db.employee_information():
                        managers.append(row["Name"])
                    managers_choice = ttk.OptionMenu(employee_frame, new_manager, *managers)
                    managers_choice.grid(row=2, column=12)

                    def change_maneger():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.change_manager(search_e, new_manager.get())
                        else:
                            pass

                    change_bu = ttk.Button(employee_frame, text="change manager", command=change_maneger)
                    change_bu.grid(row=3, column=12, sticky="snew")

                    debarment_choice_variable = StringVar()
                    debarments = [""]
                    for row in db.get_deparment():
                        debarments.append(row["Dep_Name"])
                    debarment_choice = ttk.OptionMenu(employee_frame, debarment_choice_variable, *debarments)
                    debarment_choice.grid(row=2, column=10, stick="snew")

                    def change_dep():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.change_manager(search_e, debarment_choice_variable.get())
                        else:
                            pass

                    change_bu = ttk.Button(employee_frame, text="change department", command=change_dep)
                    change_bu.grid(row=3, column=10, sticky="snew")

                    def end_task():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            db.end_task(search_e)
                            messagebox.showinfo(title="BY BY", message=f"{name} IS ENDED TASK")
                        else:
                            pass

                    if not (db.end_day(search_e) is None):
                        pass
                    else:
                        end_task_bu = ttk.Button(employee_frame, text="END TASK", command=end_task)
                        end_task_bu.grid(row=2, column=8, sticky="snew")

                    def delete_employee():
                        sure = messagebox.askquestion("hi", "Are you sure")
                        if sure == "yes":
                            id = search_e
                            if id == "":
                                messagebox.showinfo(title="ERROR", message="you can't delete me")
                            else:
                                x = db.employee_name(id)
                                for row in x:
                                    try:
                                        db.delete_employee(id)
                                        messagebox.showinfo(title="DONE", message=f"{row['Name']} has been removed")
                                    except Exception:
                                        print(row['Name'])
                                        messagebox.showinfo(title="ERROR",
                                                            message=f"there is no one have this number{id}")

                    delete_bu = ttk.Button(employee_frame, text="Delete", command=delete_employee)
                    delete_bu.grid(row=2, column=0, sticky="snew")
                except Exception:
                    messagebox.showinfo(title="ERROR", message=f"there is no employee with this id({search_e})")

    search_entry.bind("<Return>", search_bind)
    search_bu = ttk.Button(main_window, text="search", command=search)
    search_bu.grid(row=0, column=2)

    def add_employee_window():
        # style the window
        add_employee = Tk()
        add_employee.title("ADD EMPLOYEE")
        add_employee.configure(background='#e1d8b2')
        add_employee_window_style = ttk.Style()
        add_employee_window_style.theme_use("classic")
        add_employee_window_style.configure('TLabel', background='#e1d8b2')
        add_employee_window_style.configure('TButton', background='#e1d8b2')
        add_employee_window_style.configure('TRadiobutton', background='#e1d8b2')
        add_employee_window_style.configure('TLabelframe', background='#e1d8b2')

        # design the window
        name_label = ttk.Label(add_employee, text="Full Name:").grid(row=0, column=0, padx=10, pady=10)
        full_name = ttk.Entry(add_employee, width=30)
        full_name.grid(row=0, column=1)
        error1 = ttk.Label(add_employee)
        error1.grid(row=1, column=0, columnspan=3)

        identification_lapel = ttk.Label(add_employee, text="id: ").grid(row=2, column=0, padx=10, pady=10)
        identification_entry = ttk.Entry(add_employee, width=30)
        identification_entry.grid(row=2, column=1)
        error3 = ttk.Label(add_employee)
        error3.grid(row=3, column=0, columnspan=3)

        debarment_lapel = ttk.Label(add_employee, text="Debarment: ").grid(row=4, column=0, pady=10)
        debarment_choice_variable = StringVar()
        debarments = [""]
        for row in db.get_deparment():
            debarments.append(row["Dep_Name"])
        debarment_choice = ttk.OptionMenu(add_employee, debarment_choice_variable, *debarments)
        debarment_choice.grid(row=4, column=0, columnspan=3, pady=10)
        debarment_choice_error = Label(add_employee)
        debarment_choice_error.grid(row=5, column=0, columnspan=3)

        manager_lapel = ttk.Label(add_employee, text="Manager: ").grid(row=6, column=0, pady=10)
        manager_choice_variable = StringVar()
        managers = ["", ]
        for row in db.employee_information():
            managers.append(row["Name"])
        managers_choice = ttk.OptionMenu(add_employee, manager_choice_variable, *managers)
        managers_choice.grid(row=6, column=0, columnspan=3, pady=10)
        managers_choice_error = Label(add_employee)
        managers_choice_error.grid(row=7, column=0, columnspan=3)

        phone_label = ttk.Label(add_employee, text="Phone Number:").grid(row=8, column=0, padx=10, pady=10)
        phone_entry = ttk.Entry(add_employee, width=30)
        phone_entry.grid(row=8, column=1, padx=10, pady=10)
        phone_entry_error = Label(add_employee)
        phone_entry_error.grid(row=9, column=0, columnspan=3)

        salary_label = ttk.Label(add_employee, text="salary:").grid(row=10, column=0, padx=10, pady=10)
        salary_entry = ttk.Entry(add_employee, width=30)
        salary_entry.grid(row=10, column=1, padx=10, pady=10)
        salary_entry_error = Label(add_employee)
        salary_entry_error.grid(row=11, column=0, columnspan=3)

        photo_lapel = ttk.Label(add_employee, text="photo path: ").grid(row=12, column=0, padx=10, pady=10)
        photo_path_entry = ttk.Entry(add_employee, width=30)
        photo_path_entry.grid(row=12, column=1)

        def file_locate():
            # this function made for file explore and take the path
            file_path = filedialog.askopenfilename()
            photo_path_entry.delete(0, END)
            photo_path_entry.insert(0, file_path)

        photo_bu = Button(add_employee, command=file_locate, text="explore files")
        photo_bu.grid(row=12, column=2, columnspan=2)
        error4 = Label(add_employee)
        error4.grid(row=13, column=0, columnspan=3)

        submit_bu = Button(add_employee, text="submit")
        submit_bu.grid(row=14, column=0, columnspan=3)

        # check the inputs and if its not already exists and if its empty if all inputs is right it added it to the
        # data base

        def submit():
            full_name_check = full_name.get()
            name_check = False

            for char in full_name_check:
                if char.isnumeric():
                    name_check = True

            identification_check1 = identification_entry.get()
            identification_check = False

            for char in identification_check1:

                if not(char.isnumeric()):
                    identification_check = True

            path_check = False

            try:
                photo_path = open(f"{photo_path_entry.get()}", "rb")
                employee_photo = photo_path.read()
            except FileNotFoundError:
                path_check = True

            file_formula = str(photo_path_entry.get()).split(".")[-1]
            if file_formula == "png" or file_formula == "jpg" or file_formula == "rgb" or file_formula == "jpeg":
                pass
            else:
                path_check = True

            empty_id_check = identification_entry.get() == ""
            empty_name_check = full_name.get() == ""

            available_name_check = db.name_check(full_name.get())
            if not identification_check and not empty_id_check:
                available_id_check = db.identification_check(identification_entry.get())
            if empty_name_check:
                error1.config(text="THIS FILED MUST FILLED")
            else:
                if name_check:
                    error1.config(text="THIS FILED MUST NOT CONTAINING A NUMBER")
                else:
                    if available_name_check:
                        error1.config(text="THIS NAME IS ALREADY EXISTS")
                    else:
                        error1.config(text="")

            if empty_id_check:
                error3.config(text="THIS FILED MUST FILLED")
            else:
                if identification_check:
                    error3.config(text="THIS FILED MUST NOT CONTAINING A CHARACTER")
                else:
                    if available_id_check:
                        error3.config(text="THIS ID IS ALREADY EXISTS")
                    else:
                        if len(identification_entry.get()) > 9:
                            error3.config(text="YOUR ID IS MOTE THEN 9 CHARACTER")
                        else:
                            error3.config(text="")

            if path_check:
                error4.config(text="THE PATH IS INCORRECT")
            else:
                error4.config(text="")

            manager_check = False
            if manager_choice_variable.get() == "":
                managers_choice_error.config(text="this filed must be filled")
                manager_check = True
            else:
                managers_choice_error.config(text="")
                manager_check = False

            department_check = False
            if debarment_choice_variable.get() == "":
                debarment_choice_error.config(text="this filed must be filled")
                department_check = True
            else:
                debarment_choice_error.config(text="")
                department_check = False

            phone_check = False
            if phone_entry.get() == "":
                phone_entry_error.config(text="this filed must be filled")
                phone_check = True
            else:
                phone_entry_error.config(text="")
                phone_check = False

            salary = salary_entry.get()
            salary_check = False

            for char in salary:
                if not(char.isnumeric()):
                    salary_check = True

            if salary_check:
                salary_entry_error.config(text="you can't enter character")
            else:
                salary_entry_error.config(text="")

            if not empty_name_check and not empty_id_check and\
                    not name_check and not identification_check and not path_check and\
                    not available_id_check and not available_name_check\
                    and not manager_check and not department_check\
                    and not phone_check and not salary_check:
                x = db.add_employee(identification_entry.get(),
                                    full_name.get(),
                                    employee_photo,
                                    debarment_choice_variable.get(),
                                    manager_choice_variable.get(),
                                    phone_entry.get(),
                                    salary_entry.get())
                messagebox.showinfo(title="DONE", message=f"{x}")
                full_name.delete(0, END)
                identification_entry.delete(0, END)
                photo_path_entry.delete(0, END)
                add_employee.destroy()

            # if empty_password_check and empty_id_check and empty_name_check:
            #     if (name_check == False) and (identification_check == False) and (path_check == False):
            #         messagebox.showinfo(title="ERROR", message="you'r name containing a number and identification"
            #                                                    " containing"
            #                                                    " a "
            #                                                    "character and photo path is incorrect")
            #         full_name.delete(0, END)
            #         identification_entry.delete(0, END)
            #         photo_path_entry.delete(0, END)
            #     elif (name_check == False) and (identification_check == False):
            #         messagebox.showinfo(title="ERROR", message="you'r name containing a number and identification"
            #                                                    " containing"
            #                                                    " a "
            #                                                    "character")
            #         full_name.delete(0, END)
            #         identification_entry.delete(0, END)
            #     elif (name_check == False) and (path_check == False):
            #         messagebox.showinfo(title="ERROR", message="you'r name containing a number and photo path is incorrect")
            #         full_name.delete(0, END)
            #         photo_path_entry.delete(0, END)
            #     elif (identification_check == False) and (path_check == False):
            #         messagebox.showinfo(title="ERROR", message="you'r identification containing a character and photo path"
            #                                                    " is "
            #                                                    "incorrect")
            #         identification_entry.delete(0, END)
            #         photo_path_entry.delete(0, END)
            #     elif not name_check:
            #         messagebox.showinfo(title="ERROR", message="you'r name containing a number")
            #         full_name.delete(0, END)
            #     elif not identification_check:
            #         messagebox.showinfo(title="ERROR", message="you'r identification containing a character")
            #         identification_entry.delete(0, END)
            #     elif not path_check:
            #         messagebox.showinfo(title="ERROR", message="you'r photo path is incorrect")
            #         photo_path_entry.delete(0, END)
            #     else:
            #         x = db.add_employee(identification_entry.get(), full_name.get(), password_entry.get(), employee_photo)
            #         messagebox.showinfo(title="DONE", message=f"{x}")
            #         full_name.delete(0, END)
            #         identification_entry.delete(0, END)
            #         password_entry.delete(0, END)
            #         photo_path_entry.delete(0, END)
            #         add_employee.destroy()
            # else:
            #     if not empty_name_check:
            #         error1 = ttk.Label(add_employee, text="THIS FILED MUST FILLED").grid(row=1, column=0,
            #                                                                                        columnspan=2)
            #     if not empty_password_check:
            #         error2 = ttk.Label(add_employee, text="THIS FILED MUST FILLED").grid(row=3, column=0,
            #                                                                              columnspan=2)
            #     if not empty_id_check:
            #         error3 = ttk.Label(add_employee, text="THIS FILED MUST FILLED").grid(row=5, column=0,
            #                                                                              columnspan=2)

        def submit_bind(event):
            full_name_check = full_name.get()
            name_check = False

            for char in full_name_check:
                if char.isnumeric():
                    name_check = True

            identification_check1 = identification_entry.get()
            identification_check = False

            for char in identification_check1:

                if not(char.isnumeric()):
                    identification_check = True

            path_check = False

            try:
                photo_path = open(f"{photo_path_entry.get()}", "rb")
                employee_photo = photo_path.read()
            except FileNotFoundError:
                path_check = True

            file_formula = str(photo_path_entry.get()).split(".")[-1]
            if file_formula == "png" or file_formula == "jpg" or file_formula == "rgb" or file_formula == "jpeg":
                pass
            else:
                path_check = True

            empty_id_check = identification_entry.get() == ""
            empty_name_check = full_name.get() == ""

            available_name_check = db.name_check(full_name.get())
            if not identification_check and not empty_id_check:
                available_id_check = db.identification_check(identification_entry.get())
            if empty_name_check:
                error1.config(text="THIS FILED MUST FILLED")
            else:
                if name_check:
                    error1.config(text="THIS FILED MUST NOT CONTAINING A NUMBER")
                else:
                    if available_name_check:
                        error1.config(text="THIS NAME IS ALREADY EXISTS")
                    else:
                        error1.config(text="")

            if empty_id_check:
                error3.config(text="THIS FILED MUST FILLED")
            else:
                if identification_check:
                    error3.config(text="THIS FILED MUST NOT CONTAINING A CHARACTER")
                else:
                    if available_id_check:
                        error3.config(text="THIS ID IS ALREADY EXISTS")
                    else:
                        if len(identification_entry.get()) > 9:
                            error3.config(text="YOUR ID IS MOTE THEN 9 CHARACTER")
                        else:
                            error3.config(text="")

            if path_check:
                error4.config(text="THE PATH IS INCORRECT")
            else:
                error4.config(text="")

            manager_check = False
            if manager_choice_variable.get() == "":
                managers_choice_error.config(text="this filed must be filled")
                manager_check = True
            else:
                managers_choice_error.config(text="")
                manager_check = False

            department_check = False
            if debarment_choice_variable.get() == "":
                debarment_choice_error.config(text="this filed must be filled")
                department_check = True
            else:
                debarment_choice_error.config(text="")
                department_check = False

            phone_check = False
            if phone_entry.get() == "":
                phone_entry_error.config(text="this filed must be filled")
                phone_check = True
            else:
                phone_entry_error.config(text="")
                phone_check = False

            salary = salary_entry.get()
            salary_check = False

            for char in salary:
                if not(char.isnumeric()):
                    salary_check = True

            if salary_check:
                salary_entry_error.config(text="you can't enter character")
            else:
                salary_entry_error.config(text="")

            if not empty_name_check and not empty_id_check and\
                    not name_check and not identification_check and not path_check and\
                    not available_id_check and not available_name_check\
                    and not manager_check and not department_check\
                    and not phone_check and not salary_check:
                x = db.add_employee(identification_entry.get(),
                                    full_name.get(),
                                    employee_photo,
                                    debarment_choice_variable.get(),
                                    manager_choice_variable.get(),
                                    phone_entry.get(),
                                    salary_entry.get())
                messagebox.showinfo(title="DONE", message=f"{x}")
                full_name.delete(0, END)
                identification_entry.delete(0, END)
                photo_path_entry.delete(0, END)
                add_employee.destroy()

            # if empty_password_check and empty_id_check and empty_name_check:
            #     if (name_check == False) and (identification_check == False) and (path_check == False):
            #         messagebox.showinfo(title="ERROR", message="you'r name containing a number and identification"
            #                                                    " containing"
            #                                                    " a "
            #                                                    "character and photo path is incorrect")
            #         full_name.delete(0, END)
            #         identification_entry.delete(0, END)
            #         photo_path_entry.delete(0, END)
            #     elif (name_check == False) and (identification_check == False):
            #         messagebox.showinfo(title="ERROR", message="you'r name containing a number and identification"
            #                                                    " containing"
            #                                                    " a "
            #                                                    "character")
            #         full_name.delete(0, END)
            #         identification_entry.delete(0, END)
            #     elif (name_check == False) and (path_check == False):
            #         messagebox.showinfo(title="ERROR", message="you'r name containing a number and photo path is incorrect")
            #         full_name.delete(0, END)
            #         photo_path_entry.delete(0, END)
            #     elif (identification_check == False) and (path_check == False):
            #         messagebox.showinfo(title="ERROR", message="you'r identification containing a character and photo path"
            #                                                    " is "
            #                                                    "incorrect")
            #         identification_entry.delete(0, END)
            #         photo_path_entry.delete(0, END)
            #     elif not name_check:
            #         messagebox.showinfo(title="ERROR", message="you'r name containing a number")
            #         full_name.delete(0, END)
            #     elif not identification_check:
            #         messagebox.showinfo(title="ERROR", message="you'r identification containing a character")
            #         identification_entry.delete(0, END)
            #     elif not path_check:
            #         messagebox.showinfo(title="ERROR", message="you'r photo path is incorrect")
            #         photo_path_entry.delete(0, END)
            #     else:
            #         x = db.add_employee(identification_entry.get(), full_name.get(), password_entry.get(), employee_photo)
            #         messagebox.showinfo(title="DONE", message=f"{x}")
            #         full_name.delete(0, END)
            #         identification_entry.delete(0, END)
            #         password_entry.delete(0, END)
            #         photo_path_entry.delete(0, END)
            #         add_employee.destroy()
            # else:
            #     if not empty_name_check:
            #         error1 = ttk.Label(add_employee, text="THIS FILED MUST FILLED").grid(row=1, column=0,
            #                                                                                        columnspan=2)
            #     if not empty_password_check:
            #         error2 = ttk.Label(add_employee, text="THIS FILED MUST FILLED").grid(row=3, column=0,
            #                                                                              columnspan=2)
            #     if not empty_id_check:
            #         error3 = ttk.Label(add_employee, text="THIS FILED MUST FILLED").grid(row=5, column=0,
            #                                                                              columnspan=2)

        add_employee.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        add_employee.columnconfigure((0, 1, 2), weight=1)
        add_employee.bind("<Return>", submit_bind)
        submit_bu.config(command=submit)
        add_employee.mainloop()

    add_new_employee = ttk.Button(main_window, text="add new employee", command=add_employee_window)
    add_new_employee.grid(row=0, column=3, padx=60)

    def show_employees_list():
        root = Tk()
        root.title("EMPLOYERS LIST")
        dbc = DBConnect()

        # debarment_lapel = ttk.Label(add_employee, text="Debarment: ").grid(row=4, column=0, pady=10)
        # debarment_choice_variable = StringVar()
        # debarments = [""]
        # for row in db.get_deparment():
        #     debarments.append(row["Dep_Name"])
        # debarment_choice = ttk.OptionMenu(add_employee, debarment_choice_variable, *debarments)
        # debarment_choice.grid(row=4, column=0, columnspan=3, pady=10)

        filter_label = Label(root, text="filter: ").grid(row=0, column=0)

        filter_type = StringVar()
        options = ['', "Deportment", "Manager Name"]

        filter_type_options = ttk.OptionMenu(root, filter_type, *options)
        filter_type_options.grid(row=0, column=1)

        second_filter = StringVar()
        second_filter_type_options = ttk.OptionMenu(root, second_filter, '')
        second_filter_type_options.grid(row=0, column=2)
        second_filter_type_options2 = None

        def update_options(x, y, z):
            second_filter.set('')
            second_filter_type_options['menu'].delete(0, 'end')
            if filter_type.get() == "Deportment":
                new_choices_db = db.get_deparment()
                new_choices = ['', ]
                for row in new_choices_db:
                    new_choices.append(row["Dep_Name"])
            elif filter_type.get() == "Manager Name":
                new_choices_db = db.employee_information()
                new_choices = ['', ]
                for row in new_choices_db:
                    if row["Manager_Name"] in new_choices:
                        pass
                    else:
                        new_choices.append(row["Manager_Name"])

            second_filter_type_options2 = ttk.OptionMenu(root, second_filter, *new_choices)
            second_filter_type_options2.grid(row=0, column=2)

        filter_type.trace('w', update_options)

        sf = ScrolledFrame(root, width=640, height=480)
        sf.grid(sticky="snew", row=1, column=0, columnspan=4)

        # Bind the arrow keys and scroll wheel
        sf.bind_arrow_keys(root)
        sf.bind_scroll_wheel(root)

        # Create a frame within the ScrolledFrame
        inner_frame = sf.display_widget(Frame)

        def tvv(filtering):
            tv = ttk.Treeview(inner_frame)
            tv.grid(sticky="snew", row=0, column=0)
            tv.heading('#0', text='employee_number')
            tv.configure(column=('#id',
                                 '#Name',
                                 '#StartDate',
                                 '#EndDate',
                                 '#Deporment',
                                 '#Maneger_Name',
                                 '#Phone_number',
                                 '#salary',))
            tv.heading('#id', text='id')
            tv.heading('#Name', text='Name')
            tv.heading('#StartDate', text='StartDate')
            tv.heading('#EndDate', text='EndDate')
            tv.heading('#Deporment', text='Department')
            tv.heading('#Maneger_Name', text='Manager_Name')
            tv.heading('#Phone_number', text='Phone_number')
            tv.heading('#salary', text='salary')
            cursor = dbc.employee_information()
            column = 0
            for row in cursor:
                if str(filtering) == "all":
                    tv.insert('', 'end', '#{}'.format(row["employee_number"]), text=row["employee_number"])
                    tv.set('#{}'.format(row["employee_number"]), "#id", row["identification"])
                    tv.set('#{}'.format(row["employee_number"]), "#Name", row["Name"])
                    tv.set('#{}'.format(row["employee_number"]), "#StartDate", row["StartDate"])
                    tv.set('#{}'.format(row["employee_number"]), "#EndDate", row["EndDate"])
                    tv.set('#{}'.format(row["employee_number"]), "#Deporment", row["Department"])
                    tv.set('#{}'.format(row["employee_number"]), "#Maneger_Name", row["Manager_Name"])
                    tv.set('#{}'.format(row["employee_number"]), "#Phone_number", row["Phone_number"])
                    tv.set('#{}'.format(row["employee_number"]), "#salary", row["salary"])
                else:
                    if row["employee_number"] in filtering:
                        tv.insert('', 'end', '#{}'.format(row["employee_number"]), text=row["employee_number"])
                        tv.set('#{}'.format(row["employee_number"]), "#id", row["identification"])
                        tv.set('#{}'.format(row["employee_number"]), "#Name", row["Name"])
                        tv.set('#{}'.format(row["employee_number"]), "#StartDate", row["StartDate"])
                        tv.set('#{}'.format(row["employee_number"]), "#EndDate", row["EndDate"])
                        tv.set('#{}'.format(row["employee_number"]), "#Deporment", row["Department"])
                        tv.set('#{}'.format(row["employee_number"]), "#Maneger_Name", row["Manager_Name"])
                        tv.set('#{}'.format(row["employee_number"]), "#Phone_number", row["Phone_number"])
                        tv.set('#{}'.format(row["employee_number"]), "#salary", row["salary"])
                    else:
                        pass

            def on_double_click(event):
                item = tv.selection()[0]
                search_entry.insert(0, item[1:])
                search()
                search_entry.delete(0, END)
            tv.bind("<Double-Button-1>", on_double_click)

        def filters():
            if second_filter.get() == "":
                tvv("all")
            elif filter_type.get() == "Deportment":
                em = db.employee_information()
                ids = []
                for row in em:
                    if row["Department"] == second_filter.get():
                        ids.append(row["employee_number"])
                    else:
                        pass
                tvv(ids)
            elif filter_type.get() == "Manager Name":
                em = db.employee_information()
                ids = []
                for row in em:
                    if row["Manager_Name"] == second_filter.get():
                        ids.append(row["employee_number"])
                    else:
                        pass
                tvv(ids)

        filters()

        filter_button = ttk.Button(root, text="filter", command=filters)
        filter_button.grid(row=0, column=3)

        root.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        root.columnconfigure((0, 1, 2, 3), weight=1)
        root.mainloop()

    employee_list_bu = ttk.Button(main_window, text="employees list", command=show_employees_list)
    employee_list_bu.grid(row=0, column=5, padx=30)

    def show_departments_list():
        root = Tk()
        root.title("DEPARTMENTS LIST")
        dbc = DBConnect()
        sf = ScrolledFrame(root, width=640, height=480)
        sf.pack(fill="both")

        # Bind the arrow keys and scroll wheel
        sf.bind_arrow_keys(root)
        sf.bind_scroll_wheel(root)

        # Create a frame within the ScrolledFrame
        inner_frame = sf.display_widget(Frame)

        tv = ttk.Treeview(inner_frame)
        tv.grid(sticky="snew")
        tv.heading('#0', text='Dep_id')
        tv.configure(column=('#Dep_Name', '#Maneger'))
        tv.heading('#Dep_Name', text='Department Name')
        tv.heading('#Maneger', text='Manager')
        cursor = dbc.get_deparment()
        for row in cursor:
            tv.insert('', 'end', '#{}'.format(row["Dep_id"]), text=row["Dep_id"])
            tv.set('#{}'.format(row["Dep_id"]), "#Dep_Name", row["Dep_Name"])
            tv.set('#{}'.format(row["Dep_id"]), "#Maneger", row["Manager"])

        def on_double_click(event):
            item = tv.selection()[0]
            search_entry.insert(0, item[1:])
            search_entry.insert(1, "dep")
            search()
            search_entry.delete(0, END)

        tv.bind("<Double-Button-1>", on_double_click)
        root.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        root.columnconfigure((0, 1, 2, 3), weight=1)
        root.mainloop()

    dep_list_bu = ttk.Button(main_window, text="departments list", command=show_departments_list)
    dep_list_bu.grid(row=0, column=6, padx=30)

    # delete_frame = ttk.Labelframe(main_window, height=0, width=0, text="Delete Employee")
    # delete_frame.grid(row=1, column=3)
    # id_label = ttk.Label(delete_frame, text="employee number:").grid(row=0, column=0)
    # the_id = ttk.Entry(delete_frame, width=30)
    # the_id.grid(row=0, column=1)
    #
    #
    # def delete_employee():
    #     x = the_id.get()
    #     if x == "":
    #         messagebox.showinfo(title="ERROR", message="you can't delete me")
    #     else:
    #         for row in x:
    #             try:
    #                 x = db.employee_name(the_id.get())
    #                 messagebox.showinfo(title="DONE", message=f"{row['Name']} has been removed")
    #                 db.delete_employee(the_id.get())
    #                 the_id.delete(0, END)
    #             except Exception:
    #                 messagebox.showinfo(title="ERROR", message=f"there is no one have this number{row['Name']}")
    #
    #
    # delete_bu = ttk.Button(delete_frame, text="delete employee", command=delete_employee)
    # delete_bu.grid(row=1, column=0, columnspan=2)

    # def update_pass():
    #     update_password_window = Tk()
    #     update_password_window.title("UPDATE EMPLOYEE")
    #     add_style = ttk.Style()
    #     add_style.theme_use("classic")
    #     update_password_window.configure(background='#e1d8b2')
    #     add_style.configure('TLabel', background='#e1d8b2')
    #     add_style.configure('TButton', background='#e1d8b2')
    #     add_style.configure('TRadiobutton', background='#e1d8b2')
    #     add_style.configure('TLabelframe', background='#e1d8b2')
    #
    #     identification_lapel1 = ttk.Label(update_password_window, text="employee number:").grid(row=0, column=0, padx=10,
    #                                                                                             pady=10)
    #     identification_entry1 = ttk.Entry(update_password_window, width=30)
    #     identification_entry1.grid(row=0, column=1)
    #
    #     old_password_lapel = ttk.Label(update_password_window, text="old password: ").grid(row=1, column=0, padx=10,
    #                                                                                        pady=10)
    #     old_password_entry = ttk.Entry(update_password_window, width=30, show="*")
    #     old_password_entry.grid(row=1, column=1)
    #
    #     new_password_lapel = ttk.Label(update_password_window, text="new password: ").grid(row=2, column=0, padx=10,
    #                                                                                        pady=10)
    #     new_password_entry = ttk.Entry(update_password_window, show="*", width=30)
    #     new_password_entry.grid(row=2, column=1)
    #
    #     new_password_check_lapel = ttk.Label(update_password_window, text="confirm new password: ").grid(row=3, column=0,
    #                                                                                                      padx=10, pady=10)
    #     new_password_check_entry = ttk.Entry(update_password_window, show="*", width=30)
    #     new_password_check_entry.grid(row=3, column=1)
    #
    #     def submit():
    #
    #         ip = identification_entry1.get()
    #         old_pass = old_password_entry.get()
    #         new_pass = new_password_entry.get()
    #         new_pass_check = new_password_check_entry.get()
    #
    #         user = db.search_by_employee_number(ip)
    #         for row in user:
    #             original_password = row["Password"]
    #             if original_password == old_pass:
    #                 if new_pass == new_pass_check:
    #                     db.update_password(ip, new_pass)
    #                     messagebox.showinfo(title="DONE", message="new password has been updated")
    #                 else:
    #                     messagebox.showinfo(title="ERROR", message="new password confirm is incorrect")
    #             else:
    #                 messagebox.showinfo(title="ERROR", message="old password is incorrect")
    #
    #     def submit_bind(event):
    #
    #         ip = identification_entry1.get()
    #         old_pass = old_password_entry.get()
    #         new_pass = new_password_entry.get()
    #         new_pass_check = new_password_check_entry.get()
    #
    #         user = db.search_by_employee_number(ip)
    #         for row in user:
    #             original_password = row["Password"]
    #             if original_password == old_pass:
    #                 if new_pass == new_pass_check:
    #                     db.update_password(ip, new_pass)
    #                     messagebox.showinfo(title="DONE", message="new password has been updated")
    #                 else:
    #                     messagebox.showinfo(title="ERROR", message="new password confirm is incorrect")
    #             else:
    #                 messagebox.showinfo(title="ERROR", message="old password is incorrect")
    #
    #     update_password_window.bind("<Return>", submit_bind)
    #     submit_bu = ttk.Button(update_password_window, text="submit", command=submit)
    #     submit_bu.grid(row=4, column=0, columnspan=2)
    #     update_password_window.mainloop()
    #
    #
    # update_pass_bu = ttk.Button(main_window, text="update Employee password", command=update_pass)
    # update_pass_bu.grid(row=1, column=4)

    def add_dep():
        add_new_dep_window = Tk()
        add_new_dep_window.title("add new deparment")

        main_style.theme_use("classic")
        add_new_dep_window.configure(background='#e1d8b2')
        main_style.configure('TLabel', background='#e1d8b2')
        main_style.configure('TButton', background='#e1d8b2')
        main_style.configure('TRadiobutton', background='#e1d8b2')
        main_style.configure('TLabelframe', background='#e1d8b2')

        manager_lapel = ttk.Label(add_new_dep_window, text="Manager: ").grid(row=2, column=0, pady=10)
        manager_choice_variable = StringVar()
        managers = ["", ]
        for row in db.employee_information():
            managers.append(row["Name"])
        managers_choice = ttk.OptionMenu(add_new_dep_window, manager_choice_variable, *managers)
        managers_choice.grid(row=2, column=1, pady=10)
        managers_choice_error = ttk.Label(add_new_dep_window)
        managers_choice_error.grid(row=3, column=0, columnspan=2)

        name_lapel = ttk.Label(add_new_dep_window, text="Name: ").grid(row=0, column=0, sticky="snew")
        name_entry = ttk.Entry(add_new_dep_window)
        name_entry.grid(row=0, column=1)
        name_entry_error = ttk.Label(add_new_dep_window)
        name_entry_error.grid(row=1, column=0, columnspan=2)

        def submit():
            name = name_entry.get()
            manager = manager_choice_variable.get()
            manager_check = True
            name_check = True
            if manager == "":
                managers_choice_error.config(text="this must be fill")
                manager_check = False
            else:
                manager_check = True
                managers_choice_error.config(text="")

            if name == "":
                name_entry_error.config(text="this must be fill")
                name_check = False
            else:
                name_entry_error.config(text="")
                name_check = True
            if name_check and manager_check:
                db.add_deparment(name, manager)
                messagebox.showinfo(title="DONE", message="data is submitted")

        submit_bu = ttk.Button(add_new_dep_window, text="submit", command=submit)
        submit_bu.grid(row=4, column=0, columnspan=2)
        add_new_dep_window.mainloop()

    add_deparment_bu = ttk.Button(main_window, text="add new deparment", command=add_dep)
    add_deparment_bu.grid(row=0, column=4, padx=30)

    main_window.rowconfigure((0, 1), weight=1)
    main_window.columnconfigure((0, 1, 2, 3, 4), weight=1)
    main_window.mainloop()


app()

