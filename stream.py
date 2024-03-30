import streamlit as st
from PIL import Image
import requests

languages_data = {
    'Python': {
        'description': 'Python is a high-level programming language known for its simplicity and readability.',
        'features': ['Data analysis', 'Web development', 'Machine learning']
    },
    'Java': {
        'description': 'Java is a widely used programming language known for its platform independence.',
        'features': ['Enterprise applications', 'Android development', 'Web applications']
    },
    'C': {
        'description': 'C is a procedural programming language known for its efficiency and low-level capabilities.',
        'features': ['System programming', 'Embedded systems', 'Game development']
    },
    'C++': {
        'description': 'C++ is an extension of the C programming language with added features like object-oriented programming.',
        'features': ['Game development', 'System software', 'High-performance applications']
    },
    'JavaScript': {
        'description': 'JavaScript is a scripting language commonly used for web development.',
        'features': ['Front-end development', 'Back-end development', 'Web applications']
    },
    'Ruby': {
        'description': 'Ruby is a dynamic, object-oriented programming language known for its simplicity and productivity.',
        'features': ['Web development', 'Prototyping', 'Automation']
    },
    'Go': {
        'description': 'Go, also known as Golang, is a statically typed language developed by Google.',
        'features': ['Concurrency', 'Systems programming', 'Cloud services']
    },
    'Swift': {
        'description': 'Swift is a programming language developed by Apple for iOS, macOS, watchOS, and tvOS development.',
        'features': ['iOS app development', 'macOS app development', 'Cross-platform development']
    },
    'PHP': {
        'description': 'PHP is a server-side scripting language commonly used for web development.',
        'features': ['Server-side scripting', 'Web applications', 'Content management systems']
    },
    'Rust': {
        'description': 'Rust is a systems programming language known for its safety, concurrency, and performance.',
        'features': ['Systems programming', 'WebAssembly', 'Embedded systems']
    },
    'Kotlin': {
        'description': 'Kotlin is a statically typed programming language developed by JetBrains for modern multiplatform applications.',
        'features': ['Android app development', 'Web applications', 'Native applications']
    },
    'TypeScript': {
        'description': 'TypeScript is a typed superset of JavaScript that compiles to plain JavaScript.',
        'features': ['Front-end development', 'Back-end development', 'Web applications']
    },
    'Scala': {
        'description': 'Scala is a general-purpose programming language designed to be concise, elegant, and scalable.',
        'features': ['Big data processing', 'Concurrent programming', 'Web applications']
    },
    'Perl': {
        'description': 'Perl is a high-level, general-purpose programming language known for its text processing capabilities.',
        'features': ['Text processing', 'System administration', 'Web development']
    },
    'dart': {
        'description': 'dart is a statically typed programming language developed by Google.',
        'features': ['Concurrency', 'Systems programming', 'Cloud services']
    }
}

# Streamlit app
st.title('Programming Languages Overview')
st.text('created by prabit joshi')
img = Image.open("mypic.jpg")
st.image(img, width=200)

# Sidebar for language selection
selected_language = st.sidebar.selectbox('Select a programming language', list(languages_data.keys()))

# Display description and features of the selected language
if selected_language:
    st.subheader(selected_language)
    st.write('**Description:**', languages_data[selected_language]['description'])
    st.write('**Key Features:**')
    for feature in languages_data[selected_language]['features']:
        st.write(f'- {feature}')
#click button for file information
show_about_file= st.button("click me ")
if show_about_file:
 st.subheader("sorry ")

show_about_file = True

if show_about_file:
 if st.button("About File"):
        st.write("only txt file contains some information")

# Define the data for different programming languages

def fetch_github_file(url):
    response = requests.get(url)
    return response.content if response.status_code == 200 else None

# GitHub file URL (replace with your GitHub raw file URL)
github_file_url = "https://raw.githubusercontent.com/DeveloperPrabit/prabit/main/file.txt"

# Usage
if st.button("Download File"):
    file_content = fetch_github_file(github_file_url)
    if file_content:
        st.download_button(label="Download now", data=file_content, file_name="file.txt")
        file_path = r"C:\Users\prabi\OneDrive\Desktop\backend\RESUM_DEV.pdf"
file_name_Resume = "RESUM_DEV.pdf"
if st.button("Download Resume"):
      download_file_with_button(file_path, file_name_Resume)
    else:
        st.error("Failed to fetch file from GitHub. Please check the URL.")
        
