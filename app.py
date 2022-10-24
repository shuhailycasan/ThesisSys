import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
from streamlit_option_menu import option_menu
from predict_page import show_predict
from visual_page import show_visual
import streamlit_authenticator as stauth

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
def login_user1():
    c.execute('SELECT * FROM userstable WHERE username AND password')
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
def get_password(password):
    c.execute('SELECT * FROM userstable WHERE password="{}"'.format(username))
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

with st.sidebar:
    choice = option_menu(
        menu_title = "Menu",
        options= ["Home","Login","Signup"],
        icons =["house","box-arrow-in-right","person-plus-fill"],
        default_index = 0,
        key = "myform"
    )

if choice == "Home":
    st.title("Welcome to our Recommendation System")
    st.write("Please signup first")

    image = Image.open('logodwcl.jpg')
    new_image = image.resize((500, 500))
    st.image(new_image)

elif choice == "Login":
    # placeholder = st.empty()
    #
    # with st.form("my_form"):
    #     st.markdown("#### Enter your credentials")
    #     username = st.text_input("Email")
    #     password = st.text_input("Password", type="password")
    #     submit = st.form_submit_button("Login")
    #
    #     create_usertable()
    #     result = login_user(username, password)
    # if submit and result:
    #     placeholder.empty()
    # users = login_user1()
    # username =[user[1] for user in users]
    # password = [user[2] for user in users]
    #
    # credentials = {"usernames": {}}
    #
    # for un,pw in zip(username,password):
    #     user_dict = {"passwords": pw}
    #     credentials["usernames"].update({un: user_dict})
    #
    # authenticator = stauth.Authenticate(credentials, "app", "auth", cookie_expiry_days =30)
    #
    # usernames, authentication_status, passwords = authenticator.login("Login", "sidebar")
    username = st.sidebar.text_input("Username ")
    password = st.sidebar.text_input("Password ", type='password')
    load = st.sidebar.button('Login')
    if "load_state" not in st.session_state:
        st.session_state.load_state = False

    if load or st.session_state.load_state:
        st.session_state.load_state = True
        create_usertable()
        result = login_user(username, password)
        if result:
            page = st.selectbox("Choose functions", ("Recommend", "Explore"))
            if page == "Recommend":
                show_predict()

            elif page == "Explore":
                show_visual()
        else:
            st.error("Incorrect Password or Username")


elif choice == "Signup":
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
            st.balloons()
            st.success("Password verified")
            st.success("You have successfully create a valid account")
            st.info("Go to Login Menu to Log in")
