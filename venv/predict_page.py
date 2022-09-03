import numpy as np
import streamlit as st
from visual_page import show_visual

def show_predict():
    st.title("DWCL Recommendation System for Incomming College Students")
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
        course = {"Bachelor of Science in Pysychology",
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
    st.write("**Please Rate how interest are you in in this courses**")
    q1 =st.slider("1. Bachelor of Science in Computer Science", 0,10,2)
    st.markdown("""
            The **Bachelor of Computer Science or Bachelor of Science in Computer Science** is a type of bachelor's degree awarded after collegiate study in computer science. In general, computer science degree programs emphasize the mathematical and theoretical foundations of computing.
            > If you have any skills like this then this is for you
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
    q2 =st.slider("2. Bachelor of Science in Information Technology", 0, 10, 2)
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
    q3 =st.slider("3. Bachelor of Science in Civil Engineer", 0, 10, 2)
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
    q4 = st.slider("4. Bachelor of Science in Hospital Management", 0, 10, 2)
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
    q5 = st.slider("5. Bachelor of Science in Nursing", 0, 10, 2)
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
    q6 = st.slider("6. Bachelor of Science in Electrical Engineering", 0, 10, 2)
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
    q7 = st.slider("7. How well is your cooking skill?", 0, 10, 2)
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
    q8 = st.slider("8. Bachelor of Science in Business Management", 0, 10, 2)
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
    q9 = st.slider("9. Bachelor of Science in Psychology", 0, 10, 2)
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
    q10 = st.slider("10. Bachelor of Science in Management Accounting", 0, 10, 2)
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
    q11 = st.slider("11. Bachelor of Science in Elementary Education", 0, 10, 2)
    st.markdown("""
            The Bachelor of Elementary Education (BEED) is a four-year undergraduate degree program designed to prepare students to become elementary school teachers. The BEED degree program aims to develop highly motivated and competent teachers specializing in the content and pedagogy for elementary education.                
            > If you have any skills like this then this is for you:
            - Patience
            - Time management
            - Leadership
            - Communication
            - Organization
            - Self management skills
            - Independent work Skills
            > If you are also interest in this field:
            - Manager/Director – Data Analytics
            - Accounting Manager
            - Staff Accountant
            - Financial Analyst
            - Vice President – Financial Planning & Analysis (FP&A)
            - Treasurer
            and so much more :tada:
             """)

    if st.button("Recommend Course"):
        X = np.array([[question1,question2,question3,question4,question5
                       ,question6,question7,question8,question9,question10]])

