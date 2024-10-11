import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd

# Load the trained model and label encoder
model = joblib.load('career_prediction_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')


# Create the main window
root = tk.Tk()
root.title("Career Prediction System")
root.geometry("800x600")  # Adjusted window size

# Add a canvas and scrollbar for the main content
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Frame for Class 10 Marks
frame_class10 = ttk.LabelFrame(scrollable_frame, text="Class 10 Marks")
frame_class10.pack(fill="both", padx=20, pady=10)

# Class 10 subjects: Mathematics, Science, English
ttk.Label(frame_class10, text="Mathematics:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_class10_math = ttk.Entry(frame_class10)
entry_class10_math.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame_class10, text="Science:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_class10_science = ttk.Entry(frame_class10)
entry_class10_science.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame_class10, text="English:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
entry_class10_english = ttk.Entry(frame_class10)
entry_class10_english.grid(row=2, column=1, padx=10, pady=5)

# Frame for Class 12 Marks
frame_class12 = ttk.LabelFrame(scrollable_frame, text="Class 12 Marks")
frame_class12.pack(fill="both", padx=20, pady=10)

# Class 12 subjects: Mathematics, Physics, Chemistry, Biology, English
ttk.Label(frame_class12, text="Mathematics:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_class12_math = ttk.Entry(frame_class12)
entry_class12_math.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame_class12, text="Physics:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_class12_physics = ttk.Entry(frame_class12)
entry_class12_physics.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame_class12, text="Chemistry:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
entry_class12_chemistry = ttk.Entry(frame_class12)
entry_class12_chemistry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(frame_class12, text="Biology:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
entry_class12_biology = ttk.Entry(frame_class12)
entry_class12_biology.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(frame_class12, text="English:").grid(row=4, column=0, padx=10, pady=5, sticky='w')
entry_class12_english = ttk.Entry(frame_class12)
entry_class12_english.grid(row=4, column=1, padx=10, pady=5)

# Frame for College Subjects Marks
frame_college = ttk.LabelFrame(scrollable_frame, text="College Subjects Marks")
frame_college.pack(fill="both", padx=20, pady=10)

# List of college subjects
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

# Dictionary to hold entry fields for college subjects
college_entries = {}
for idx, subject in enumerate(college_subjects):
    ttk.Label(frame_college, text=f"{subject}:").grid(row=idx//2, column=(idx % 2) * 2, padx=10, pady=5, sticky='w')
    entry = ttk.Entry(frame_college)
    entry.grid(row=idx//2, column=(idx % 2) * 2 + 1, padx=10, pady=5)
    college_entries[subject] = entry

# Function to collect and predict career based on input marks
def predict_job_role():
    try:
        # Collect Class 10 marks
        class10_marks = {
            'Mathematics': float(entry_class10_math.get() or 0),
            'Science': float(entry_class10_science.get() or 0),
            'English': float(entry_class10_english.get() or 0),
            'Hindi': float(entry_class10_english.get() or 0),
            'Social Science': float(entry_class10_english.get() or 0)
        }
        
        # Collect Class 12 marks
        class12_marks = {
            'Mathematics': float(entry_class12_math.get() or 0),
            'Physics': float(entry_class12_physics.get() or 0),
            'Chemistry': float(entry_class12_chemistry.get() or 0),
            'Biology': float(entry_class12_biology.get() or 0),
            'English': float(entry_class12_english.get() or 0)
        }
        
        # Collect College Subject marks
        college_marks = {subject: float(entry.get() or 0) for subject, entry in college_entries.items()}
        
        # Combine all marks into a single input vector
        input_data = {**class10_marks, **class12_marks, **college_marks}
        input_df = pd.DataFrame([input_data])
        
        # Debugging: Print the input data
        print(input_df)
        
        # Predict job role using the ML model
        job_role_encoded = model.predict(input_df)[0]
        job_role = label_encoder.inverse_transform([job_role_encoded])[0]
        
        # Display the predicted job role
        messagebox.showinfo("Predicted Job Role", f"The predicted job role is: {job_role}")
        
    except ValueError as e:
        print(f"Error: {e}")
        messagebox.showerror("Input Error", "Please enter valid numerical marks.")

# Submit button
submit_button = ttk.Button(root, text="Predict Job Role", command=predict_job_role)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
