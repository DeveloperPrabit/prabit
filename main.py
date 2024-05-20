# import module
import streamlit as st
import subprocess
import admin

# import Image from pillow to open images
from PIL import Image

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('signup_data.db')
cursor = conn.cursor()

# Create a table to store signup data if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (username TEXT PRIMARY KEY, email TEXT, password TEXT)''')
conn.commit()

# Title
st.title("Hello welcome to frontend using python!!!")

st.button("Click me for no reason")

if st.button("About Me", key='about_me_button'):
    st.text("Developed By Prabit Joshi!!!")

status = st.radio("Select Gender: ", ('Male', 'Female'), key='gender_radio')

if st.checkbox("Show/Hide_Image", key='show_hide_image'):
    img = Image.open("mypic.jpg")
    st.image(img, width=200)
    st.caption("This is a caption")

if status == 'Male':
    st.write("You selected Male")
elif status == 'Female':
    st.write("You selected Female")

hobby = st.selectbox("Hobbies: ", ['Coding', 'Gaming', 'Sports'], key='hobbies_selectbox')
st.write("Your hobby is: ", hobby)

# Initialize session state variables
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'page' not in st.session_state:
    st.session_state.page = 'Sign In'

def signup():
    st.title('Sign Up')

    # Input fields for username, email, and password with unique keys
    username = st.text_input('Username', key='signup_username_input')
    email = st.text_input('Email', key='signup_email_input')
    password = st.text_input('Password', type='password', key='signup_password_input')

    # Button to submit the signup form
    if st.button('Sign Up', key='signup_button'):
        try:
            # Check if username already exists in the database
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                st.error('Username already exists. Please choose a different username.')
            else:
                # Insert new user into the database
                cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
                conn.commit()  # Commit changes to the database
                st.success('You have successfully signed up! Proceed to sign in.')
        except Exception as e:
            st.error(f'An error occurred: {e}')

def signin():
    st.title('Sign In')

    # Input fields for username and password with unique keys
    username = st.text_input('Username', key='signin_username_input')
    password = st.text_input('Password', type='password', key='signin_password_input')

    # Button to submit the sign-in form
    if st.button('Sign In', key='signin_button'):
        try:
            # Check if username exists in the database and passwords match
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            existing_user = cursor.fetchone()
            if existing_user:
                st.success('You have successfully signed in!')
                st.session_state.authenticated = True  # Set authentication status to True
                st.session_state.page = 'Home'  # Redirect to Home page after successful sign-in
                navigate_to_main_page()
            else:
                st.error('Invalid username or password. Please try again.')
        except Exception as e:
            st.error(f'An error occurred: {e}')

def navigate_to_main_page():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio('Go to:', ['Home', 'Profile', 'Settings'], key='main_navigation_radio')

    if selection == 'Home':
        st.session_state.page = 'Home'
        home_page()
    elif selection == 'Profile':
        st.session_state.page = 'Profile'
        profile_page()
    elif selection == 'Settings':
        st.session_state.page = 'Settings'
        settings_page()

def home_page():
    st.title('Home')
    st.write('Welcome to the Home page!')

def profile_page():
    st.title('Profile')
    st.write('This is your profile page.')

def settings_page():
    st.title('Settings')
    st.write('Here you can update your settings.')

def main():
    if st.session_state.authenticated:  # Show navigation options if authenticated
        navigate_to_main_page()
    else:  # Show sign-up and sign-in pages if not authenticated
        page = st.sidebar.radio('Navigate:', ['Sign Up', 'Sign In', 'Admin'], key='page_navigation_radio')
        if page == 'Sign Up':
            signup()
        elif page == 'Sign In':
            signin()
        elif page == 'Admin':
            st.write('Welcome to the admin system')
            subprocess.run(['streamlit', 'run', 'admin.py'])

if __name__ == '__main__':
    main()
    # Close the database connection
    conn.close()
    st.write('Thanks for using Streamlit!')
    st.balloons()
    st.header("Created by prabit joshi")

# Subheader
st.subheader("development using python")
# Text
st.text("Come to learn!!!")
# Markdown
st.markdown("### Thank you for your attention!")
