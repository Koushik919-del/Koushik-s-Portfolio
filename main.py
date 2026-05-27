# app.py
import streamlit as st
import streamlit.components.v1 as components
import os
from constant import *

# 1. Page Configuration
st.set_page_config(
    page_title=f"{info['name']} | Portfolio", 
    page_icon="🏠", 
    layout="wide",
    initial_sidebar_state="collapsed"
) 

# 2. Main Page Layout Wrapper (Centering content with padding columns)
margin_r, body, margin_l = st.columns([0.4, 3, 0.4])

with body:
    menu() # Custom navigation menu if defined in constant.py

    # Sidebar Fallback
    with st.sidebar:
        st.success("Navigate through the pages above.")
        
    # --- HERO / ABOUT ME SECTION ---
    st.header("About Me", divider='rainbow')

    col1, col2, col3 = st.columns([1.3, 0.2, 1])

    with col1:
        st.write(info['brief'])
        st.markdown(f"###### 😄 Name: {info['name']}")
        st.markdown(f"###### 👉 Study: {info['study']}")
        st.markdown(f"###### 📍 Location: {info['location']}")
        st.markdown(f"###### 📚 Interest: {info['interest']}")
        st.markdown("###### 🟡 Favorite Color: Yellow")
        st.markdown(f"###### 👀 LinkedIn: [{info['name']}]({linkedin_link})")
        
        # Safe Resume Downloader (Won't crash if file is missing)
        resume_path = "src/resume.pdf"
        if os.path.exists(resume_path):
            with open(resume_path, "rb") as file:
                pdf_file = file.read()

            st.download_button(
                label="Download my :blue[resume] 📄",
                data=pdf_file,
                file_name=f"{info['name'].replace(' ', '_')}_Resume.pdf",
                mime="application/pdf"
            )
        else:
            st.info("💡 Add your resume to `src/resume.pdf` to enable the download button.")

    with col3:
        # Safe Image Loader (Uses a fallback placeholder if your photo isn't ready)
        portrait_path = "src/portrait.jpeg"
        if os.path.exists(portrait_path):
            st.image(portrait_path, width=360)
        else:
            st.image("https://via.placeholder.com/360x360.png?text=Your+Portrait+Here", width=360)

    st.write("---")

    # --- SKILLS GRID SECTION ---
    st.subheader("My :blue[skills] ⚒️", divider='rainbow')

    def skill_tab():
        # Calculate dynamic rows based on skill list length and desired columns
        total_skills = len(info['skills'])
        rows = total_skills // skill_col_size
        if total_skills % skill_col_size != 0:
            rows += 1
            
        skills_iterator = iter(info['skills'])
        
        for x in range(rows):
            columns = st.columns(skill_col_size)
            for index_ in range(skill_col_size):
                try:
                    # Renders each skill as a clean, wide button
                    columns[index_].button(next(skills_iterator), use_container_width=True)
                except StopIteration:
                    break

    # Loading state wrapping the grid renderer
    with st.spinner(text="Loading section..."):
        skill_tab()
