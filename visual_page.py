import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def show_visual():
    st.title("Visualization of the Study")
    #barchart
    #--------------COLLEGE STUDENTS DATA VISUALIZATION------
    st.header("College Sophomore")
    st.subheader("Numbers of Students who participated in our Studies")
    data1 = {"Courses":["Bachelor of Science in Civil Engineering",
                        "Bachelor of Science in Electrical Engineering",
                        "Bachelor of Science in Information Technology",
                        "Bachelor of Science in Computer Science",
                        "Bachelor of Science in Library and Information Science",
                        "Bachelor of Science in Accountancy",
                        "Bachelor of Science in Management Accounting"],
                        "Students Participated":[10,5,10,10,14,10,5]}
    data1 = pd.DataFrame(data1)
    data1 = data1.set_index("Courses")
    st.bar_chart(data1)


    # Pie Chart
    st.subheader("Percentage of Students if they are confindent in finishing their degree")
    data1 = {"Yes or No": ["Yes", "No"],
             "Percentage": [76.9, 23.1 ]}
    data1 = pd.DataFrame(data1)
    data1 = data1.set_index("Yes or No")
    st.bar_chart(data1)


    #Pie Chart
    st.subheader("Reason why they are not confident in their chosen degree")
    labels = 'Financial Problem', 'The Course is hard', 'they are not sure'
    sizes = [49.2, 31.5, 20.3]
    explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    # Pie Chart
    st.subheader("Did you choose your course on your own accord?")
    labels = 'Yes', 'No'
    sizes = [92.3, 7.7]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    # Pie Chart
    st.subheader("What pushes them to choose this course")
    labels = 'because of friends', 'parents decisions','no choice'
    sizes = [50.9, 29.1,20]
    explode = (0, 0.1,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    #piechart
    st.subheader("they are sometimes want to shift courses")
    labels = 'No', 'Yes'
    sizes = [69.2, 30.8]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    # piechart
    st.subheader("The cause of their desire to change course")
    labels = 'Hard Course', 'they struggle','never expect to that course they choose is hard'
    sizes = [50.1, 39.1,10]
    explode = (0, 0.1,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)
    #--------------SENIOR HIGH STUDENTS DATA VISUALIZATION-----------
    st.header("College Sophomore")
    st.subheader("Numbers of Students who participated in our Studies")

    #------CORRELATION MATRIX OF SENIOR HIGH AND COLLEGE STUDENTS--------
    #st.subheader("The Correlation Matrix of Senior High and College Students")
    # con = pd.read_csv('cor3.csv')
    # fig, ax = plt.subplots()
    # sns.heatmap(con.corr(method='pearson'),annot=True, ax=ax)
    # st.write(fig)
