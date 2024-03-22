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



