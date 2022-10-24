import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
from streamlit_option_menu import option_menu
from predict_page import show_predict
from visual_page import show_visual
import streamlit_authenticator as stauth
from app import create_usertable,add_userdata,login_user,view_all_users,view_unique_username,get_username,edit_username_data


## DATABASE CONNECTION
import sqlite3
conn = sqlite3.connect('data2.db')
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT,department TEXT, course TEXT)')

def create_admintable():
    c.execute('CREATE TABLE IF NOT EXISTS admintable(username TEXT, password TEXT,position TEXT)')

def add_userdata(username,password,department,course):
    c.execute('INSERT INTO userstable(username, password,department,course) VALUES (?,?,?,?)',(username,password,department,course))
    conn.commit()

def add_admindata(username,password,position):
    c.execute('INSERT INTO admintable(username, password,position) VALUES (?,?,?)',(username,password,position))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username,password))
    data = c.fetchall()
    return data

def login_admin(username,password):
    c.execute('SELECT * FROM admintable WHERE username = ? AND password = ?', (username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def login_admin1():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def view_all_admins():
    c.execute('SELECT * FROM admintable')
    data = c.fetchall()
    return data

def view_unique_username():
    c.execute('SELECT DISTINCT username FROM userstable')
    data = c.fetchall()
    return data

def view_unique_username_admin():
    c.execute('SELECT DISTINCT username FROM admintable')
    data = c.fetchall()
    return data

def get_username(username):
    c.execute('SELECT * FROM userstable WHERE username="{}"'.format(username))
    data = c.fetchall()
    return data

def get_username_admin(username):
    c.execute('SELECT * FROM adminstable WHERE username="{}"'.format(username))
    data = c.fetchall()
    return data

def edit_username_data(username,password,department,course,update_user,update_pass,update_department,update_course):
    c.execute("UPDATE userstable SET username = ?, password = ?, department = ?, course = ? WHERE username = ? and password = ? and department = ? and course = ?",(update_user,update_pass,update_department,update_course,username,password,department,course))
    conn.commit()
    data = c.fetchall()
    return data

def edit_username_data_admin(username,password,position,update_user,update_pass,update_position):
    c.execute("UPDATE admintable SET username = ?, password = ?, position = ? WHERE username = ? and password = ? and position = ?",(update_user,update_pass,update_position,username,password,position))
    conn.commit()
    data = c.fetchall()
    return data

with st.sidebar:
    choice = option_menu(
        menu_title = "Menu",
        options= ["Home","Login","Signup"],
        icons =["house","box-arrow-in-right","person-plus-fill"],
    )
if choice == "Home":
    st.title("Welcome to our Recommendation System")
    st.write("Please signup first")

    image = Image.open('logodwcl.jpg')
    new_image = image.resize((500, 500))
    st.image(new_image)

elif choice == "Login":
    # users = login_admin1()
    # username = [user[1] for user in users]
    # password = [user[2] for user in users]
    #
    # credentials = {"usernames": {}}
    #
    # for un, pw in zip(username, password):
    #     user_dict = {"passwords": pw}
    #     credentials["usernames"].update({un: user_dict})
    #
    # authenticator = stauth.Authenticate(credentials, "app", "auth", cookie_expiry_days=30)
    #
    # usernames, authentication_status, passwords = authenticator.login("Login", "sidebar")
    username = st.sidebar.text_input("Username ")
    password = st.sidebar.text_input("Password ", type='password')
    load = st.sidebar.button('Login')
    if "load_state" not in st.session_state:
        st.session_state.load_state = False

    if load or st.session_state.load_state:
        st.session_state.load_state = True
        create_admintable()
        result = login_admin(username,password)
        if result:
            # authenticator.logout("Logout", "sidebar")
            page = st.selectbox("Choose functions", ("Explore","Users"))

            if page == "Explore":
                show_visual()

            elif page == "Users":

                st.subheader("View All Users")
                user_result = view_all_users()
                clean_db = pd.DataFrame(user_result, columns=["Username", "Password", "Department", "Course"])
                with st.expander("View All Data"):
                    st.dataframe(clean_db)

                st.subheader("View All Admins")
                user_result1 = view_all_admins()
                clean_db3 = pd.DataFrame(user_result1, columns=["Username", "Password", "Position"])
                with st.expander("View All Data"):
                    st.dataframe(clean_db3)

                menu = ["Add","Edit"]
                choice = st.selectbox("Add and Edit users", menu)

                if choice == "Add":
                    menu1 = ["Students", "Admins"]
                    choice1 = st.selectbox("Students or Admins", menu1)
                    if choice1 == "Students":
                        add_user = st.text_input("Username")
                        add_pass = st.text_input("Password", type='password')
                        add_department = {"ABM", "STEM", "HUMSS", "TVL", "GAS","N/A"}
                        add_department = st.selectbox("Select your SHS Strand", add_department)

                        if add_department == "ABM":
                            st.write("Accountancy, Business and Management")
                            add_course = {"ABM"}
                            add_course = st.selectbox("SHS STRAND", add_course)

                        elif add_department == "GAS":
                            st.write("General Academic Strand")
                            add_course = {"GAS"}
                            add_course = st.selectbox("SHS STRAND", add_course)

                        elif add_department == "HUMSS":
                            st.write("Humanities and Social Sciences")
                            add_course = {"HUMSS"}
                            add_course = st.selectbox("SHS STRAND", add_course)

                        elif add_department == "STEM":
                            st.write("Science, Technology, Engineering")
                            add_course = {"STEM for Mathematics and Engineering", "STEM for Health and Sciences"}
                            add_course = st.selectbox("SHS STRAND", add_course)
                        elif add_department == "TVL":
                            st.write("Technical - Vocational - Livelihood Track")
                            add_course = {"Cookery",
                                      "Bread and Pastry Production (NCII)",
                                      "Food and Beverage Services (NCII)",
                                      "Computer Systems Servicing"}
                            add_course = st.selectbox("SHS STRAND", add_course)
                        else:
                            add_course = st.write("N/A")

                        if st.button("Add User"):
                            create_usertable()
                            add_userdata(add_user, add_pass, add_department, add_course)
                            st.success("You have successfully add user")

                    if choice1 == "Admins":
                        add_user = st.text_input("Username")
                        add_pass = st.text_input("Password", type='password')
                        add_position = st.text_input("Position")
                        if st.button("Add User"):
                            create_admintable()
                            add_admindata(add_user, add_pass, add_position)
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
                with st.expander("View Updated Data"):
                    st.subheader("UPDATED DATA")
                    st.dataframe(clean_db2)

                with st.expander("Most User"):
                    departmentdf = clean_db2['Department'].value_counts().to_frame()
                    departmentdf = departmentdf.reset_index()

                    st.subheader("Most User of the Recommendation System")
                    p1=px.pie(departmentdf,names ='index', values='Department')
                    st.plotly_chart(p1)
        else:
            st.warning("Incorrect Password or Username")

elif choice == "Signup":
    st.subheader("Create New Account")
    st.subheader("For Admins Only")
    new_user =st.text_input("Username")
    new_pass =st.text_input("Password",type= 'password')
    position =st.text_input("Position")

    if st.button('Sign up'):
        if len(new_pass) < 6:
            st.warning("The Password must be at least minimum of 6 characters")
        if new_user == '':
            st.warning("The Username Field is Empty")
        else:
            create_admintable()
            add_admindata(new_user,new_pass,position)
            st.success("Password verified")
            st.success("You have successfully create a valid account")
            st.info("Go to Login Menu to Log in")