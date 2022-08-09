import streamlit as st
from visual_page import show_visual


def show_predict():
    st.title("DWCL Recommendation System for Incomming College Students")

    st.write("""### Please Rate so we can predict your Reccomended Courses""")

    department = {"SOECS","SBMA","SEAS","SHOM"}

    department =st.selectbox("Select your department", department)

    if department == "SOECS":
        st.write("School of Engineering and Computer Studies(SOECS)")
        course ={"Bachelor of in Information Technology",
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
        course = st.selectbox("SBMA COURSES", course)

    elif department == "SHOM":
        st.write("School of Hospitality Management(SHOM) and School of Nursing(SON)")
        course = {"Bachelor of Science in Hospital Management",
                       "Bachelor of Science in Nursing"}
        course = st.selectbox("SBMA COURSES", course)

    st. write("Please Rate 1 to 10 wisely")
    question1 =st.slider("Do you like Reading?", 0,10,2)
    question2 =st.slider("Do you play any sports?", 0, 10, 2)
    question3 =st.slider("Do you love playing computer games?", 0, 10, 2)
    question4 = st.slider("Do you love Math", 0, 10, 2)
    question5 = st.slider("Do you Science?", 0, 10, 2)
    question6 = st.slider("Are you sometime curios about you upbringing in life", 0, 10, 2)

    button =st.button("Recommend Course")
