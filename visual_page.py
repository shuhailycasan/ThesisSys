import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def show_visual():
    st.title("Visualization of the Study")
    #1.
    #barchart
    #--------------COLLEGE STUDENTS DATA VISUALIZATION-------------
    st.header("College Sophomore")
    st.subheader("Numbers of Students who participated in our Studies")
    data1 = {"Courses":["Bachelor of Science in Computer Science",
                        "Bachelor of Science in Psychology",
                        "Bachelor of Science in Information Technology",
                        "Bachelor of Science in Management Accounting",
                        "Bachelor of Science in Library and Information Science",
                        "Bachelor of Science in Accountancy",
                        "Others"],
                        "Students Participated":[4,2,4,2,2,2,5]}
    data1 = pd.DataFrame(data1)
    data1 = data1.set_index("Courses")
    st.bar_chart(data1)

    # 2.
    # Pie Chart
    st.subheader("Percentage of Students if they are confident in finishing their degree")
    data1 = {"Yes or No": ["Yes", "No"],
             "Percentage": [84.4, 17.6 ]}
    data1 = pd.DataFrame(data1)
    data1 = data1.set_index("Yes or No")
    st.bar_chart(data1)

    # 3.
    #Pie Chart
    st.subheader("Reason why they are not confident in their chosen degree")
    labels = 'Financial Problem', 'The course is hard', 'they are not sure'
    sizes = [49.2, 31.5, 20.3]
    explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    # 4.
    # Pie Chart
    st.subheader("Percentage if they choose the course on their own accord?")
    labels = 'Yes', 'No'
    sizes = [88.2, 11.8]
    explode = (0, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    # 5.
    # Pie Chart
    st.subheader("Reason what pushes them to choose this course")
    labels = 'because of friends', 'parents decisions','no choice'
    sizes = [39.5, 30.3,29.2]
    explode = (0, 0.1,0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    #6.
    #piechart
    st.subheader("Percentage If They sometimes want to shift courses")
    labels = 'No', 'Yes'
    sizes = [70.6, 29.4]
    explode = (0, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    #7.
    # piechart
    st.subheader("The causes of their desire to change course")
    labels = 'Struggling in their chosen course','Financial Difficulty'
    sizes = [60.1, 39.9]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)


    #--------------SENIOR HIGH STUDENTS DATA VISUALIZATION-----------
    #1.
    st.header("Senior High Students")
    st.subheader("Numbers of Students who participated in our Studies")
    data1 = {"Courses": ["STEM",
                         "GAS",
                         "TVL",
                         "ABM",
                         "HUMSS"],
             "Students Participated": [5, 3, 4, 5, 4]}
    data1 = pd.DataFrame(data1)
    data1 = data1.set_index("Courses")
    st.bar_chart(data1)

    # 2.
    # Pie Chart
    st.subheader("Percentage of Students if they are confident in taking their chosen course")
    data1 = {"Yes or No": ["Yes", "No"],
             "Percentage": [76.2, 23.8]}
    data1 = pd.DataFrame(data1)
    data1 = data1.set_index("Yes or No")
    st.bar_chart(data1)

    # 3.
    # Pie Chart
    st.subheader("Reason why they are not confident in their chosen degree")
    labels = 'Did not learn much in online class', 'They are not sure if they will enroll','Choose to work'
    sizes = [40.2, 39.5, 20.3]
    explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    # 4.
    # Pie Chart
    st.subheader("Percentage if they choose the course on their own accord?")
    labels = 'Yes', 'No'
    sizes = [90.5, 9.5]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    #5.
    # Pie Chart
    st.subheader("If no, what pushes them to choose the course")
    labels = 'The parents chose their course','Family choose their course'
    sizes = [50,50]
    explode = (0,0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    #------CORRELATION MATRIX OF SENIOR HIGH AND COLLEGE STUDENTS--------
    #st.subheader("The Correlation Matrix of Senior High and College Students")
    # con = pd.read_csv('cor3.csv')
    # fig, ax = plt.subplots()
    # sns.heatmap(con.corr(method='pearson'),annot=True, ax=ax)
    # st.write(fig)
