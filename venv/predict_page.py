import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
from visual_page import show_visual

def show_predict():
    st.title("DWCL Recommendation System")
    st.subheader("for Incomming College Students")
    st.caption("By: Shuhaily Casan and Nicky Palero")

    #Select courses
    department = {"SOECS","SBMA","SEAS","SHOM"}
    department =st.selectbox("Select your department", department)
    if department == "SOECS":
        st.write("School of Engineering and Computer Studies(SOECS)")
        course ={"Bachelor of Science in Information Technology",
                       "Bachelor of Science in Computer Science",
                       "Bachelor of Science in Civil Engineering",
                        "Bachelor of Science in Electrical Engineering",
                       "Bachelor of Science in Library and Information Science"}
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
        course = {"Bachelor of Science in Psychology",
                       "Bachelor of Physical Education",
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


    #Course Assesment Rating Scale
    st.write("")
    st.write("")
    st.markdown("""### **Course Assessment**""")
    st.write("**Please rate how interested are you in in this 17 courses by reading the Assessments**")
    image = Image.open('likertScale.PNG')
    new_image = image.resize((670, 80))
    st.image(new_image)
    st.write("")

    st.write("")
    st.write("**1. Bachelor of Science in Computer Science**")
    q1 =st.slider("",0,5,2)
    st.markdown("""
            The **Bachelor of Computer Science or Bachelor of Science in Computer Science** is a type of bachelor's degree awarded after collegiate study in computer science. In general, computer science degree programs emphasize the mathematical and theoretical foundations of computing.
            > If you have any skills like this then this is for you,
            - Theoritical
            - Mathematics
            - Computer and Technological Skills
            - Analysis Person
            > If you are also interest in this field:
            - Software Development
            - Game Development
            - Machine Learning Engineer
            - Data Scientist
                """)


    q2 =st.slider("2. Bachelor of Science in Information Technology", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Science in Information Technology (BSIT)** program is a four-year degree program which focuses on the study of computer utilization and computer software to plan, install, customize, operate, manage, administer and maintain information technology infrastructure.                
            > If you have any skills like this then this is for you:
            - Creative Person
            - Problem Solving
            - Management
            - Computer literacy
            - Analysis Abilities
            > If you are also interest in this field:
            - Web Development
            - systems analyst
            - Network architect
            - Database administrator
            - Information security analyst
            and so much more :tada:
                    """)


    q3 =st.slider("3. Bachelor of Science in Civil Engineer", 0, 5, 2)
    st.markdown("""
            A **Bachelor of Science in Civil Engineering (BSCE)** is intended to provide graduates with the skills and knowledge needed to design, build, and operate engineered systems such as roads, foundations, buildings, bridges, dams, airports, and water supply and wastewater treatment systems.                    
            > If you have any skills like this then this is for you:
            - Critical Thinker
            - Collaborative Person
            - Technical skills
            - Project Management
            - Creativity and flexibility
            > If you are also interest in this field:
            - Consulting civil Engineer
            - CAD Technician
            - Design Engineer
            - Contractor
            - Building COntrol Surveyor
            and so much more :tada:
                        """)


    q4 = st.slider("4. Bachelor of Science in Hospital Management", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Science in Hospitality Management (BSHM)** is a degree program that delivers education to people who are interested to build a career in the leisure industry involving the planning, development, implementation and control of culinary and accommodation/billeting operations.                        
            > If you have any skills like this then this is for you:
            - Teamwork Skills
            - Leadership Skills
            - Organization Skills
            - an Empath Person
            - Communication skill
            > If you are also interest in this field:
            - Hotel Manager
            - Accommodation manager
            - Catering manager
            - Chef
            - Conference centre manager
            and so much more :tada:
            """)


    q5 = st.slider("5. Bachelor of Science in Nursing", 0, 5, 2)
    st.markdown("""
            The Bachelor of Science in Nursing (BSN) is a four-year degree program that teaches students the necessary skills and knowledge for health care. It revolves around four main components; health promotion, disease prevention, risk reduction, and health restoration. The program aims to develop nursing students who are capable of providing holistic care to individuals of different ages, gender, and health statuses. 
            > If you have any skills like this then this is for you:
            - Professionalism
            - Critical thinking and creative problem solving.
            - Attitude and confidence
            - Communication
            - Empath Person
            - Conflict resolution
            > If you are also interest in this field:
            - Nursing Superintendent
            - Industrial Nurse
            - Military Nurse
            - Home Care Nurses
            - Community Health Nurse (CHN)
            -Industrial Nurse.
            and so much more :tada:
             """)


    q6 = st.slider("6. Bachelor of Science in Electrical Engineering", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Science in Electrical Engineering** is a five-year degree program that focuses on conceptualizing, developing, and designing a safe, economical, and ethical utilization of electrical energy. The program also trains students to effectively develop and test real-life applications of electrical circuitry, digital systems, electrical equipment, and machinery control.           
            > If you have any skills like this then this is for you:
            - Critical Thinker
            - Technical Skills
            - Creativity and flexibility
            - Project Management. 
            - Communication Skills
            > If you are also interest in this field:
            - Electrical technician
            - Electrician
            - Test engineer
            - Electrical designer
            - Electrical engineer
            and so much more :tada:
             """)


    q7 = st.slider("7. Bachelor of Library and Information Science", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Library and Information Science (BLIS)** is a four-year program that prepares students in the development, deployment, and management of information resources in print, non-print, electronic, and digital formats.            
            > If you have any skills like this then this is for you:
            - Management Skills
            - Computer Skills
            - Professionalism
            - Documentation Skills
            - Critical Thinking
            > If you are also interest in this field:
            - Librarian
            - Library Information Assistant
            - Storage Specialist
            - Archivist
            - Abstractor.
            and so much more :tada:
             """)


    q8 = st.slider("8. Bachelor of Science in Business Management", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Science in Business Administration** is a four-year program that focuses on managing businesses and their overall operations. The program involves critical decision-making skills in order to successfully strategize business operations.            
            > If you have any skills like this then this is for you:
            - Time Management
            - Communication Skills
            - Technology Skills
            - Analytical Skills
            - Organizational Skills
            > If you are also interest in this field:
            - Financial Analyst
            - Sales Manager
            - Business Consultant
            - Business Consultant
            - Loan Officer
            - Meeting, Convention and Event Planner
            and so much more :tada:
             """)


    q9 = st.slider("9. Bachelor of Science in Psychology", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Science in Business Administration** is a four-year program that focuses on managing businesses and their overall operations. The program involves critical decision-making skills in order to successfully strategize business operations.            
            > If you have any skills like this then this is for you:
            - Patience & Active Listening
            - Communication Skills
            - Critical Thinking
            - Creative Problem-Solving
            - Time Management
            > If you are also interest in this field:
            - Clinical psychologist 
            - Education mental health
            - Counselling psychologist
            - Forensic psychologist
            - Educational psychologist
            - Education mental health practitionerr
            and so much more :tada:
             """)


    q10 = st.slider("10. Bachelor of Science in Management Accounting", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Science in Management Accounting** is a four-year degree program that provides students with knowledge and skills in management. It includes discussions on the systems, procedures, and policies relevant to company management and decisions. The program also aims to produce globally competitive students who are capable of applying both accounting and management techniques.            
            > If you have any skills like this then this is for you:
            - Accounting skills
            - Presentation skills
            - Flexibility and adaptability
            - Technical skills
            - Documentation and report writing skills
            -Leadership and collaboration
            > If you are also interest in this field:
            - Manager/Director – Data Analytics
            - Accounting Manager
            - Staff Accountant
            - Financial Analyst
            - Vice President – Financial Planning & Analysis (FP&A)
            - Treasurer
            and so much more :tada:
             """)


    q11 = st.slider("11. Bachelor of Science in Elementary Education", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Elementary Education (BEED)** is a four-year undergraduate degree program designed to prepare students to become elementary school teachers. The BEED degree program aims to develop highly motivated and competent teachers specializing in the content and pedagogy for elementary education.                
            > If you have any skills like this then this is for you:
            - Patience
            - Time management
            - Leadership
            - Communication
            - Organize person
            - Self management skills
            - Independent work Skills
            > If you are also interest in this field:
            - Teacher
            - Curriculum Developer
            - Researcher
            - Academic Advisor
            - School Administrator
            - College Professor
            and so much more :tada:
             """)


    q12 = st.slider("12. Bachelor of Science in Internal Auditing", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Science in Internal Auditing (BSIA)** is a four year degree program that provides general accounting education to students wanting to pursue a professional career in Internal Auditing. BSIA hones professionals who can enhance and protect organizational value by providing stake holders with risk-based, objective and reliable assurance, advise and insight                
            > If you have any skills like this then this is for you:
            - Management Skills
            - Problem Solver
            - Leadership
            - Risk Management Skills
            - Organization
            - Self management skills
            > If you are also interest in this field:
            - Auditing specialists
            - Risk assessment specialists
            - Financial analysts
            - Lead internal auditors
            - Information systems auditors
            - Internal controls auditors
            and so much more :tada:
             """)


    q13 = st.slider("13. Bachelor of Science in Accounting", 0, 5, 2)
    st.markdown("""
            A **Bachelor of Science (BS) in Accounting** is four-year degree that requires more courses related to the accounting major to prepare students for entry-level positions in corporate, nonprofit, or government accounting.            
            > If you have any skills like this then this is for you:
            - Time Management Skills
            - Critical Thinking Skills
            - Analytical
            - Communication Skills
            - Emotional Intelligence
            - Professionalism
            > If you are also interest in this field:
            - Staff Accountant
            - Loan Officer.
            - Financial analysts
            - Management Accountant
            - Information systems auditors
            - Financial Analyst.
            and so much more :tada:
             """)


    q14 = st.slider("14. Bachelor of Physical Education", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Physical Education** is a four-year degree program in the Philippines that will train you in developing and maintaining the optimal physical fitness and functionality individuals                
            > If you have any skills like this then this is for you:
            - Athletic Ability
            - Presentation Skills
            - Problem Solving
            - Critical Thinking
            - Communication Skills
            - Calm and Empath
            - Initiative
            > If you are also interest in this field:
            - Adaptive Physical Education Specialist
            - Athletic Director
            - Aerobics Instructo
            - Adventure/Outdoor Educator
            - Fitness and Recreation Manager / Consultant
            - Fitness, and Wellness Facilities Manager
            and so much more :tada:
             """)


    q15 = st.slider("15. Bachelor of Secondary Education", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Secondary Education** (BSED) is a four year degree program designed to prepare students for becoming high school teachers. The program combines both theory and practice in order to teach students the necessary knowledge and skills a high school teacher needs. The program aims to produce competent teachers who provide a conducive learning experience to their students.                 
            > If you have any skills like this then this is for you:
            - Study Skills
            - Collaboration skills
            - Communication skills
            - Critical Thinking
            - Communication Skills
            - Presentation Skills
            - Leadership Skills
            > If you are also interest in this field:
            - Teaching assistant
            - Subject teacher
            - English as a Second Language (ESL) Teacher.
            - High school teacher
            - Education administrator
            and so much more :tada:
             """)


    q16 = st.slider("16. Bachelor of Special Needs Education", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Special Needs Education (BSNEd)** is a four-year undergraduate program of the 2018 curriculum which aims to prepare aspiring teachers in the field of special needs education. Specifically, the program aims to develop highly competent special education (SPED) teacher-researchers who specialize in providing and managing instruction to students with additional needs in an inclusive and / or segregated setting.            > If you have any skills like this then this is for you:
            - Patience
            - Organize
            - Creativity
            - Intuitive and Calming Nature
            - Communication Skills
            - Presentation Skills
            > If you are also interest in this field:
            - Special Education Teacher (Secondary School)
            - Educational Specialist
            - Special Education Paraprofessional
            - Special Education Teacher (Preschool, Kindergarten, or Elementary School)
            and so much more :tada:
             """)


    q17 = st.slider("16. Bachelor of Human Services", 0, 5, 2)
    st.markdown("""
            The **Bachelor of Special Needs Education (BSNEd)** is a four-year undergraduate program of the 2018 curriculum which aims to prepare aspiring teachers in the field of special needs education. Specifically, the program aims to develop highly competent special education (SPED) teacher-researchers who specialize in providing and managing instruction to students with additional needs in an inclusive and / or segregated setting.            > If you have any skills like this then this is for you:
            - Empathy
            - Active listening
            - Organization skills
            - Patience
            - Communication Skills
            - Cultural competence
            - Critical Thinking
            > If you are also interest in this field:
            - Community health worker.
            - Case manager
            - Behavioral therapist
            - Probation officer
            - Child adoption specialist
            - Substance abuse counselor
            and so much more :tada:
             """)

    if st.button("Recommend Course"):

        df = pd.read_csv("book1.csv")

        corrMatrix = df.corr(method='pearson')
        corrMatrix.head(17)


        def get_similar(question, rating):
            similar_ratings = corrMatrix[question] * (rating - 2.5)
            similar_ratings = similar_ratings.sort_values(ascending=False)
            return similar_ratings

        c1 = "Bachelor of Science in Civil Engineering"
        c2 = "Bachelor of Science in Electrical Engineering"
        c3 = "Bachelor of Science in Information Technology"
        c4 = "Bachelor of Science in Computer Science"
        c5 = "Bachelor of Science in Library and Information Science"
        c6 = "Bachelor of Science in Accountancy"
        c7 = "Bachelor of Science in Management Accounting"
        c8 = "Bachelor of Science in internal Auditing"
        c9 = "Bachelor of Science in Business Administration"
        c10 = "Bachelor of Science in Psychology"
        c11 = "Bachelor of Physical Education"
        c12 = "Bachelor of Elementary Education"
        c13 = "Bachelor of Secondary Education"
        c14 = "Bachelor of Special Needs Education"
        c15 = "Bachelor in Human Needs"
        c16 = "Bachelor of Science in Hospital Management"
        c17 = "Bachelor of Science in Nursing"

        ratings = [(c1, q1), (c2, q2), (c3, q3), (c4, q4), (c5, q5), (c6, q6), (c7, q7), (c8, q8), (c9, q9), (c10, q10),
                   (c11, q11), (c12, q12), (c13, q13), (c14, q14), (c15, q15), (c16, q16), (c17, q17)]


        similar = pd.DataFrame()

        for question, rating in ratings:
             similar=similar.append(get_similar(question, rating), ignore_index=True)

             similar.head(10)

        st.header("Course Assessment Results")
        st.write("**The three DWCL courses that are most suitable for you**")
        st.write(similar.sum().sort_values(ascending=False).head(3),600,200)
