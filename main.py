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

if(st.button("About Me")):
	st.text("Welcome To Prabits Development!!!")


status = st.radio("Select Gender: ", ('Male', 'Female'))

if st.checkbox("Show/Hide_Image"):
    img = Image.open("mypic.jpg")
    st.image(img, width=200)
    st.caption("This is a caption")

if status == 'Male':
        st.write("You selected Male")
elif status == 'Female':
        st.write("You selected Female")
hobby = st.selectbox("Hobbies: ",
                     ['Coding', 'Gaming', 'Sports'])
 

st.write("Your hobby is: ", hobby)


# Global variable to track authentication status
authenticated = False

def signup():
    st.title('Sign Up')

    # Input fields for username, email, and password with unique keys
    username = st.text_input('Username', key='signup_username_input')
    email = st.text_input('Email', key='signup_email_input')
    password = st.text_input('Password', type='password', key='signup_password_input')

    # Button to submit the signup form
    if st.button('Sign Up'):
        try:
            # Check if username already exists in the database
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                st.error('Username already exists. Please choose a different username.')
            else:
                # Insert new user into the database
                cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                               (username, email, password))
                conn.commit()  # Commit changes to the database
                st.success('You have successfully signed up! Proceed to sign in.')
        except Exception as e:
            st.error(f'An error occurred: {e}')

def signin():
    global authenticated  # Use the global variable

    st.title('Sign In')

    # Input fields for username and password with unique keys
    username = st.text_input('Username', key='signin_username_input')
    password = st.text_input('Password', type='password', key='signin_password_input')

    # Button to submit the sign-in form
    if st.button('Sign In'):
        try:
            # Check if username exists in the database and passwords match
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            existing_user = cursor.fetchone()
            if existing_user:
                st.success('You have successfully signed in!')
                authenticated = True  # Set authentication status to True
                # Redirect to main page after successful sign-in
                navigate_to_main_page()
            else:
                st.error('Invalid username or password. Please try again.')
        except Exception as e:
            st.error(f'An error occurred: {e}')

def navigate_to_main_page():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio('Go to:', ['Home', 'Profile', 'Settings'])

    if selection == 'Home':
        st.write('Welcome to the main page!')
    elif selection == 'Profile':
        st.write('This is your profile page.')
    elif selection == 'Settings':
        st.write('Here you can update your settings.')


def main():
    global authenticated  # Use the global variable

    page = st.sidebar.radio('Navigate:', ['Sign Up', 'Sign In', 'Admin'])

    if not authenticated:  # Show sign-up and sign-in pages if not authenticated
        if page == 'Sign Up':
            signup()
        elif page == 'Sign In':
            signin() 
        elif page == 'Admin':
            st.write('Welcome to the admin system')
            subprocess.run(['streamlit', 'run', 'admin.py'])   
    else:  # If authenticated, show main page
        navigate_to_main_page()
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
