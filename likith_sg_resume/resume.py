import os
import pkg_resources

def get_resume_path():
    try:
        resume_path = pkg_resources.resource_filename(__name__, 'likith-sg-resume.pdf')
        return resume_path
    except Exception as e:
        print(f"Error retrieving the resume: {e}")
        return None

def display_resume():
    resume_path = get_resume_path()
    if resume_path:
        print(f"Your resume is available at: {resume_path}")
    else:
        print("Could not locate the resume file.")
  
