# constant.py

# Navigation Menu placeholder (if you don't have a multi-page setup yet)
def menu():
    pass  # Streamlit 1.30+ handles multi-page natively via the 'pages/' folder, 
          # but we keep this function here so your main code doesn't crash.

# Social links
linkedin_link = "https://www.linkedin.com/in/yourprofile"
github_link = "https://github.com/yourusername"

# Control the grid size for your skills section
skill_col_size = 4

# All your personal portfolio details
info = {
    "name": "Your Name Here",
    "study": "B.S. Computer Science / Robotics Engineering",
    "location": "California, USA",
    "interest": "AI Automation, Hardware Hacking, Rapid Prototyping",
    "brief": """
    I'm an engineer and builder specializing in the intersection of intelligent software 
    and physical hardware. I love turning complex logic into real-world applications 
    and fast prototypes that solve immediate problems. 
    """,
    "skills": [
        "Python", "C++", "Streamlit", "PyTorch", 
        "OpenCV", "Git", "Arduino", "Linux", 
        "CAD Design", "ROS 2", "SQL", "Docker"
    ]
}
