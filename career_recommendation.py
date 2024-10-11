import pandas as pd
import random

# Define subjects for Class 10, Class 12, and College
class10_subjects = ['Mathematics', 'Science', 'English','Hindi','Social Science']
class12_subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'English']
college_subjects = [
    "Basic Electrical Engineering", "Mathematics I", "Physics", "Analog Electronic Circuits", "Environmental Science",
    "Basic Manufacturing Systems", "Yoga and Human Consciousness", "Professional Communication", "Chemistry", "Biology",
    "Engineering Graphics", "Computer Programming", "Data Structures and Algorithms", "Digital Electronics",
    "Engineering Economics", "Object-Oriented Programming", "Probability & Statistics", "Computer Organization and Architecture",
    "Database Management Systems", "Principle of Digital Communication", "Operating Systems", "Automata and Formal Languages",
    "Web Technology", "Business Communication", "Software Engineering", "Big Data", "Design and Analysis of Algorithms",
    "High-Performance Computing", "Computer Networks", "Artificial Intelligence", "Law of Patent", "Data Analytics",
    "Internet of Things", "Compiler Design", "Software Project Management", "Cloud Computing", "Tools and Techniques Laboratory",
    "Minor Project"
]

# Define possible job roles (the full 70 roles)
job_roles = ['Software Developer', 'Data Scientist', 'Engineer', 'Full Stack Developer', 'Doctor', 'AI Researcher', 
             'Machine Learning Engineer', 'Cybersecurity Analyst', 'Database Administrator', 'Web Developer', 
             'Project Manager', 'Economist', 'Patent Lawyer', 'Data Analyst', 'Cloud Architect', 'DevOps Engineer', 
             'Software Engineer', 'Mechanical Engineer', 'Biotechnologist', 'Environmental Engineer', 'Electrical Engineer',
             'Telecommunications Engineer', 'Electronics Engineer', 'Systems Architect', 'Civil Engineer', 'Pharmacist', 
             'Aerospace Engineer', 'Network Engineer', 'Embedded Systems Engineer', 'Game Developer', 'Blockchain Developer', 
             'Robotics Engineer', 'Cloud Engineer', 'Technical Consultant', 'Systems Analyst', 'Operations Manager', 
             'Urban Planner', 'Architect', 'Biomedical Engineer', 'Chemical Engineer', 'Investment Banker', 
             'Digital Marketing Specialist', 'Technical Writer', 'AI Ethicist', 'Statistician', 'Astrophysicist', 
             'Forensic Scientist', 'Marine Biologist', 'Food Scientist', 'Geneticist', 'Quantum Computing Researcher', 
             'Bioinformatics Scientist', 'Nanotechnology Engineer']

# Function to randomly generate marks between 50 and 100
def generate_marks():
    return random.randint(50, 100)

# Complete job assignment logic based on subject marks
def assign_job_role(marks):
    # Logic based on key subjects
    if marks['Mathematics'] > 85 and marks['Computer Programming'] > 85:
        return 'Software Developer'
    elif marks['Data Analytics'] > 85:
        return 'Data Scientist'
    elif marks['Social Science']>90 and marks['Engineering Economics']>90:
        return 'Civil Services'
    elif marks['Mathematics'] > 80 and marks['Physics'] > 80:
        return 'Engineer'
    elif marks['Mathematics'] > 80 and marks['Data Structures and Algorithms'] > 80:
        return 'Full Stack Developer'
    elif marks['Biology'] > 85 and marks['Chemistry'] > 80:
        return 'Doctor'
    elif marks['Physics'] > 80 and marks['Probability & Statistics'] > 80:
        return 'AI Researcher'
    elif marks['Mathematics'] > 80 and marks['Big Data'] > 85:
        return 'Machine Learning Engineer'
    elif marks['Operating Systems'] > 80 and marks['Computer Networks'] > 80:
        return 'Cybersecurity Analyst'
    elif marks['Database Management Systems'] > 85 and marks['Software Engineering'] > 85:
        return 'Database Administrator'
    elif marks['Web Technology'] > 85 and marks['Object-Oriented Programming'] > 80:
        return 'Web Developer'
    elif marks['Business Communication'] > 80 and marks['Professional Communication'] > 80:
        return 'Project Manager'
    elif marks['Engineering Economics'] > 80 and marks['Probability & Statistics'] > 80:
        return 'Economist'
    elif marks['Law of Patent'] > 85:
        return 'Patent Lawyer'
    elif marks['Big Data'] > 85 and marks['Data Structures and Algorithms'] > 85:
        return 'Data Analyst'
    elif marks['Cloud Computing'] > 85 and marks['Operating Systems'] > 80:
        return 'Cloud Architect'
    elif marks['Compiler Design'] > 80 and marks['Software Engineering'] > 85:
        return 'DevOps Engineer'
    elif marks['Software Engineering'] > 85 and marks['Design and Analysis of Algorithms'] > 80:
        return 'Software Engineer'
    elif marks['Engineering Graphics'] > 85:
        return 'Mechanical Engineer'
    elif marks['Biology'] > 80 and marks['Chemistry'] > 80:
        return 'Biotechnologist'
    elif marks['Environmental Science'] > 80:
        return 'Environmental Engineer'
    elif marks['Physics'] > 85 and marks['Digital Electronics'] > 85:
        return 'Electrical Engineer'
    elif marks['Physics'] > 80 and marks['Principle of Digital Communication'] > 80:
        return 'Telecommunications Engineer'
    elif marks['Physics'] > 85 and marks['Analog Electronic Circuits'] > 80:
        return 'Electronics Engineer'
    elif marks['Mathematics'] > 85 and marks['Automata and Formal Languages'] > 80:
        return 'Systems Architect'
    elif marks['Physics'] > 80 and marks['Engineering Graphics'] > 80:
        return 'Civil Engineer'
    elif marks['Biology'] > 85 and marks['Chemistry'] > 80:
        return 'Pharmacist'
    elif marks['Mathematics'] > 80 and marks['Physics'] > 80:
        return 'Aerospace Engineer'
    elif marks['Mathematics'] > 85 and marks['Computer Networks'] > 85:
        return 'Network Engineer'
    elif marks['Computer Organization and Architecture'] > 85 and marks['Operating Systems'] > 85:
        return 'Embedded Systems Engineer'
    elif marks['Web Technology'] > 85 and marks['Design and Analysis of Algorithms'] > 85:
        return 'Game Developer'
    elif marks['Digital Electronics'] > 80 and marks['Design and Analysis of Algorithms'] > 85:
        return 'Robotics Engineer'
    elif marks['Cloud Computing'] > 80 and marks['Operating Systems'] > 80:
        return 'Cloud Engineer'
    elif marks['Software Project Management'] > 80 and marks['Business Communication'] > 80:
        return 'Technical Consultant'
    elif marks['Operating Systems'] > 85 and marks['Compiler Design'] > 80:
        return 'Systems Analyst'
    elif marks['Engineering Economics'] > 80 and marks['Design and Analysis of Algorithms'] > 80:
        return 'Operations Manager'
    elif marks['Engineering Economics'] > 80 and marks['Environmental Science'] > 80:
        return 'Urban Planner'
    elif marks['Engineering Graphics'] > 85:
        return 'Architect'
    elif marks['Chemistry'] > 85 and marks['Biology'] > 85:
        return 'Biomedical Engineer'
    elif marks['Physics'] > 80 and marks['Chemistry'] > 80:
        return 'Chemical Engineer'
    elif marks['Engineering Economics'] > 85 and marks['Probability & Statistics'] > 80:
        return 'Investment Banker'
    elif marks['Business Communication'] > 80 and marks['Professional Communication'] > 85:
        return 'Digital Marketing Specialist'
    elif marks['Software Engineering'] > 85 and marks['Database Management Systems'] > 85:
        return 'Technical Writer'
    elif marks['Data Analytics'] > 85 and marks['Big Data'] > 85:
        return 'AI Ethicist'
    elif marks['Probability & Statistics'] > 85 and marks['Data Analytics'] > 85:
        return 'Statistician'
    elif marks['Physics'] > 85 and marks['Digital Electronics'] > 85:
        return 'Astrophysicist'
    elif marks['Physics'] > 85 and marks['Chemistry'] > 85:
        return 'Forensic Scientist'
    elif marks['Biology'] > 85 and marks['Environmental Science'] > 85:
        return 'Marine Biologist'
    elif marks['Physics'] > 85 and marks['Chemistry'] > 85:
        return 'Food Scientist'
    elif marks['Chemistry'] > 85 and marks['Biology'] > 85:
        return 'Geneticist'
    elif marks['Probability & Statistics'] > 85 and marks['Big Data'] > 85:
        return 'Quantum Computing Researcher'
    elif marks['Physics'] > 85 and marks['Data Analytics'] > 85:
        return 'Bioinformatics Scientist'

    else:
        return random.choice(job_roles)


# Generate synthetic data for 1000 students
data = []
for _ in range(1000):
    # Generate marks for Class 10, Class 12, and College subjects
    class10_marks = {subject: generate_marks() for subject in class10_subjects}
    class12_marks = {subject: generate_marks() for subject in class12_subjects}
    college_marks = {subject: generate_marks() for subject in college_subjects}
    
    # Combine all marks
    marks = {**class10_marks, **class12_marks, **college_marks}
    
    # Assign job role
    job_role = assign_job_role(marks)
    
    # Append the data
    student_data = {**marks, 'Job Role': job_role}
    data.append(student_data)

# Convert the data into a DataFrame and save it
df = pd.DataFrame(data)
df.to_csv('student_marks_job_roles_1000.csv', index=False)

print("Synthetic dataset created and saved as 'student_marks_job_roles_1000.csv'")
