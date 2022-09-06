import streamlit as st
import pandas as pd
from PIL import Image
from predict_page import show_predict
from visual_page import show_visual


## DATABASE CONNECTION
import sqlite3
conn = sqlite3.connect('data1.db')
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT,department TEXT, course TEXT)')

def add_userdata(username,password,department,course):
    c.execute('INSERT INTO userstable(username, password,department,course) VALUES (?,?,?,?)',(username,password,department,course))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def view_unique_username():
    c.execute('SELECT DISTINCT username FROM userstable')
    data = c.fetchall()
    return data

def get_username(username):
    c.execute('SELECT * FROM userstable WHERE username="{}"'.format(username))
    data = c.fetchall()
    return data

def edit_username_data(username,password,department,course,update_user,update_pass,update_department,update_course):
    c.execute("UPDATE userstable SET username = ?, password = ?, department = ?, course = ? WHERE username = ? and password = ? and department = ? and course = ?",(update_user,update_pass,update_department,update_course,username,password,department,course))
    conn.commit()
    data = c.fetchall()
    return data



menu=["Home","Login","Sign up"]
choice =st.sidebar.selectbox("Menu", menu)
if choice == "Home":
    st.title("Welcome to our Recommendation System")
    st.write("Please signup first")

    image = Image.open('logodwcl.jpg')
    new_image = image.resize((600, 600))
    st.image(new_image)

elif choice == "Login":
        username = st.sidebar.text_input("Username ")
        password = st.sidebar.text_input("Password ",type='password')

        if st.sidebar.checkbox("Log in"):
            create_usertable()
            result = login_user(username,password)

            if result:
                st.success("Logged in as {}".format(username))
                page = st.selectbox("Choose functions", ("Predict", "Explore","Users"))

                if page == "Predict":
                    show_predict()

                elif page == "Explore":
                    show_visual()

                elif page == "Users":

                    if username == "admin" and password == "123":
                        st.subheader("View All User")
                        user_result = view_all_users()
                        clean_db = pd.DataFrame(user_result,columns=["Username","Password","Department","Course"])
                        st.dataframe(clean_db)
                        menu = ["Add","Edit"]
                        choice = st.selectbox("Add and Edit users", menu)

                        if choice == "Add":
                            add_user = st.text_input("Username")
                            add_pass = st.text_input("Password", type='password')
                            add_department = st.text_input("Department")
                            add_course =st.text_input("Course")
                            if st.button("Add User"):
                                create_usertable()
                                add_userdata(add_user, add_pass, add_department, add_course)
                                st.success("You have successfully add user")

                        elif choice == "Edit":
                            list_of_name = [i[0] for i in view_unique_username()]
                            selected_name = st.selectbox("User to Edit",list_of_name)
                            selected_result = get_username(selected_name)
                            st.write(selected_result)

                            if selected_result:
                                username = selected_result[0][0]
                                password = selected_result[0][1]
                                department = selected_result[0][2]
                                course = selected_result[0][3]

                                update_user = st.text_input("Username")
                                update_pass = st.text_input("Password", type='password')
                                update_department = st.text_input("Department")
                                update_course = st.text_input("Course")

                                if st.button("Update User"):
                                    edit_username_data(username, password, department, course, update_user, update_pass,update_department, update_course)
                                    st.success("You have successfully Updated:: {} TO ::{}".format(username,update_user))

                        updated_result = view_all_users()
                        clean_db2 = pd.DataFrame(updated_result, columns=["Username", "Password", "Department", "Course"])
                        st.subheader("UPDATED DATA")
                        st.dataframe(clean_db2)

                    else:
                        st.warning("For Admins only")
            else:
                st.warning("Incorrect Password or Username")

elif choice == "Sign up":
    st.subheader("Create New Account")
    new_user =st.text_input("Username")
    new_pass =st.text_input("Password",type= 'password')

    department = {"SOECS", "SBMA", "SEAS", "SHOM","None"}

    department = st.selectbox("Select your department", department)

    if department == "SOECS":
        st.write("School of Engineering and Computer Studies(SOECS)")
        course = {"Bachelor of in Information Technology",
                        "Bachelor of in Computer Science",
                        "Bachelor of in Civil Engineering",
                        "Bachelor of in Civil Engineering",
                        "Bachelor of Library and Information Science"}
        course = st.selectbox("SOECS COURSES", course)

    elif department == "SBMA":
        st.write("School of Business, Management, and Accountancy(SBMA)")
        course = {"Bachelor of Science in Accountancy",
                       "bachelor of Science in Management Accounting",
                       "Bachelor of Science in internal Auditing",
                       "Bachelor of Science in Business Administration"}
        course = st.selectbox("SBMA COURSES", course)

    elif department == "SEAS":
        st.write("School of Education, Arts and Science(SEAS)")
        course = {"Bachelor of Science in Pysychology",
                       "bachelor of Physical Education",
                       "Bachelor of Special Needs Education",
                       "Bachelor in Human Needs",
                       "Bachelor of Elementary Education",
                       "Bachelor of Secondary Education"}
        course = st.selectbox("SEAS COURSES", course)

    elif department == "SHOM":
        st.write("School of Hospitality Management(SHOM) and School of Nursing(SON)")
        course = {"Bachelor of Science in Hospital Management",
                          "Bachelor of Science in Nursing"}
        course = st.selectbox("SHOM COURSES", course)
    else:
        course = st.write("N/A")

    if st.button('Sign up'):
        create_usertable()
        add_userdata(new_user,new_pass,department,course)
        st.success("You have successfully create a valid account")
        st.info("Go to Login Menu to Log in")