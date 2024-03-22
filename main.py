# import module
import streamlit as st
# import Image from pillow to open images
from PIL import Image

# Title
st.title("Hello welcome to frontend using python!!!")


st.button("Click me for no reason")

if(st.button("About Me")):
	st.text("Welcome To Prabits Development!!!")


# Header
st.header("Created by prabit joshi") 

# Subheader
st.subheader("development using python")
# Text
st.text("Come to learn!!!")
# Markdown
st.markdown("### Thank you for your attention!")



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

# Page title
st.title('Sign Up')

# Input fields for username, email, and password
username = st.text_input('Username')
email = st.text_input('Email')
password = st.text_input('Password', type='password')

# Button to submit the form
if st.button('Sign Up'):
    # Validation and processing logic
    if username and email and password:
        st.success('You have successfully signed up!')
    else:
        st.error('Please fill in all the fields.')


def main():
    st.title('Sign In')

    # Input fields for username and password with unique keys
    username = st.text_input('Username', key='username_input')
    password = st.text_input('Password', type='password', key='password_input')

    # Button to submit the sign-in form
    if st.button('Sign In'):
        # Mock authentication logic (replace with actual logic)
        if username == 'user' and password == 'pass':
            st.success('You have successfully signed in!')
            # Redirect to main page after successful sign-in
            navigate_to_main_page()
        else:
            st.error('Invalid username or password. Please try again.')

def navigate_to_main_page():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio('Go to:', ['Home', 'Profile', 'Settings'])

    if selection == 'Home':
        st.write('Welcome to the main page!')
    elif selection == 'Profile':
        st.write('This is your profile page.')
    elif selection == 'Settings':
        st.write('Here you can update your settings.')

if __name__ == '__main__':
    main()
