import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
from predict_page import show_predict
from visual_page import show_visual


## DATABASE CONNECTION
import sqlite3
conn = sqlite3.connect('data2.db')
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
    new_image = image.resize((500, 500))
    st.image(new_image)

elif choice == "Login":
        username = st.sidebar.text_input("Username ")
        password = st.sidebar.text_input("Password ",type='password')

        if st.sidebar.checkbox("Log in"):
            create_usertable()
            result = login_user(username,password)

            if result:
                st.success("Logged in as {}".format(username))
                page = st.selectbox("Choose functions", ("Recommend", "Explore","Users"))

                if page == "Recommend":
                    show_predict()

                elif page == "Explore":
                    show_visual()

                elif page == "Users":

                    if username == "admin" and password == "1234567":
                        st.subheader("View All User")
                        user_result = view_all_users()
                        clean_db = pd.DataFrame(user_result, columns=["Username", "Password", "Department", "Course"])
                        with st.expander("View All Data"):
                            st.dataframe(clean_db)

                        menu = ["Add","Edit"]
                        choice = st.selectbox("Add and Edit users", menu)

                        if choice == "Add":
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
                        st.warning("For Admins only")
            else:
                st.warning("Incorrect Password or Username")

elif choice == "Sign up":
    st.subheader("Create New Account")
    new_user =st.text_input("Username")
    new_pass =st.text_input("Password",type= 'password')

    department = {"ABM", "STEM", "HUMSS", "TVL","GAS","N/A"}

    department = st.selectbox("Select your SHS Strand", department)

    if department == "ABM":
        st.write("Accountancy, Business and Management")
        course = {"ABM"}
        course = st.selectbox("SHS STRAND", course)

    elif department == "GAS":
        st.write("General Academic Strand")
        course = {"GAS"}
        course = st.selectbox("SHS STRAND", course)

    elif department == "HUMSS":
        st.write("Humanities and Social Sciences")
        course = {"HUMSS"}
        course = st.selectbox("SHS STRAND", course)

    elif department == "STEM":
        st.write("Science, Technology, Engineering")
        course = {"STEM for Mathematics and Engineering", "STEM for Health and Sciences"}
        course = st.selectbox("SHS STRAND", course)
    elif department == "TVL":
        st.write("Technical - Vocational - Livelihood Track")
        course = {"Cookery",
                  "Bread and Pastry Production (NCII)",
                  "Food and Beverage Services (NCII)",
                  "Computer Systems Servicing"}
        course = st.selectbox("SHS STRAND", course)
    else:
        course = st.write("N/A")

    if st.button('Sign up'):
        if len(new_pass) < 6:
            st.warning("The Password must be at least minimum of 6 characters")
        if new_user == '':
            st.warning("The Username Field is Empty")
        else:
            create_usertable()
            add_userdata(new_user,new_pass,department,course)
            st.success("Password verified")
            st.success("You have successfully create a valid account")
            st.info("Go to Login Menu to Log in")
