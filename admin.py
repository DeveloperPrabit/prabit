import streamlit as st
import sqlite3
import smtplib
import random
import string

# Connect to SQLite database
conn = sqlite3.connect('admin_data.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, email TEXT, password TEXT, is_admin INTEGER)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS pictures
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT UNIQUE, description TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)''')

conn.commit()

# Initialize session state variables
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def send_email(to_email, new_password):
    try:
        # Establish a secure session with Gmail's outgoing SMTP server using your Gmail account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Use your email and app password
        sender_email = "prabitjoshi@gmail.com"
        sender_password = "uexn xcad frkl bgrk"
        server.login(sender_email, sender_password)
        
        subject = "Password Reset"
        body = f"Your new password is: {new_password}"
        msg = f'Subject: {subject}\n\n{body}'
        
        server.sendmail(sender_email, to_email, msg)
        server.quit()
    except Exception as e:
        st.error(f"Failed to send email: {e}")

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    new_password = ''.join(random.choice(characters) for i in range(length))
    return new_password

def reset_password(username):
    cursor.execute("SELECT email FROM users WHERE username=? AND is_admin=1", (username,))
    user = cursor.fetchone()
    if user:
        email = user[0]
        new_password = generate_random_password()
        cursor.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
        conn.commit()
        send_email(email, new_password)
        st.success('A new password has been sent to your email.')
    else:
        st.error('Admin username not found.')

def admin_login():
    st.title('Admin Login')

    username = st.text_input('Username', key='login_username')
    password = st.text_input('Password', type='password', key='login_password')

    if st.button('Login'):
        # Check if username exists and credentials are correct
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        if user:
            if user[4] == 1:  # Check if the user is an admin (is_admin flag is 1)
                st.success('Admin login successful!')
                st.session_state.authenticated = True
                admin_dashboard()
            else:
                st.error('You do not have admin privileges.')
        else:
            st.error('Invalid username or password.')
    
    if st.button('Forgot Password'):
        reset_password(username)

def admin_dashboard():
    st.title('Admin Dashboard')

    # Sidebar options
    selected_option = st.sidebar.radio(
        'Admin Options',
        ['Add User', 'Remove User', 'Edit User', 'View Users', 'Add Picture', 'View Pictures', 'Add Post', 'View Posts', 'Exit'],
        key='admin_options_radio'  # Unique key for the radio group
    )

    if selected_option == 'Add User':
        add_user()
    elif selected_option == 'Remove User':
        remove_user()
    elif selected_option == 'Edit User':
        edit_user()
    elif selected_option == 'View Users':
        view_users()
    elif selected_option == 'Add Picture':
        add_picture()
    elif selected_option == 'View Pictures':
        view_pictures()
    elif selected_option == 'Add Post':
        add_post()
    elif selected_option == 'View Posts':
        view_posts()
    elif selected_option == 'Exit':
        st.session_state.authenticated = False
        st.session_state.page = 'Admin Login'
        st.stop()

def add_user():
    st.header('Add User')

    username = st.text_input('Username', key='add_user_username')
    email = st.text_input('Email', key='add_user_email')
    password = st.text_input('Password', type='password', key='add_user_password')
    is_admin = st.checkbox('Admin Privileges', key='add_user_checkbox')

    if st.button('Add User'):
        try:
            cursor.execute("INSERT INTO users (username, email, password, is_admin) VALUES (?, ?, ?, ?)",
                           (username, email, password, 1 if is_admin else 0))
            conn.commit()
            st.success('User added successfully.')
        except sqlite3.IntegrityError:
            st.error('Username or email already exists.')

def remove_user():
    st.header('Remove User')

    username = st.text_input('Username', key='remove_user_username')

    if st.button('Remove User'):
        cursor.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
        st.success('User removed successfully.')

def edit_user():
    st.header('Edit User')

    username = st.text_input('Username', key='edit_user_username')
    email = st.text_input('Email', key='edit_user_email')
    password = st.text_input('Password', type='password', key='edit_user_password')
    is_admin = st.checkbox('Admin Privileges', key='edit_user_checkbox')

    if st.button('Update User'):
        cursor.execute("UPDATE users SET email=?, password=?, is_admin=? WHERE username=?",
                       (email, password, 1 if is_admin else 0, username))
        conn.commit()
        st.success('User updated successfully.')

def view_users():
    st.header('View Users')

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    if users:
        for user in users:
            st.write(f"Username: {user[1]}, Email: {user[2]}, Admin: {'Yes' if user[4] == 1 else 'No'}")
    else:
        st.info('No users found.')

def add_picture():
    st.header('Add Picture')

    filename = st.text_input('Filename', key='add_picture_filename')
    description = st.text_input('Description', key='add_picture_description')

    if st.button('Add Picture'):
        try:
            cursor.execute("INSERT INTO pictures (filename, description) VALUES (?, ?)", (filename, description))
            conn.commit()
            st.success('Picture added successfully.')
        except sqlite3.IntegrityError:
            st.error('Filename already exists.')

def view_pictures():
    st.header('View Pictures')

    cursor.execute("SELECT * FROM pictures")
    pictures = cursor.fetchall()

    if pictures:
        for picture in pictures:
            st.write(f"Filename: {picture[1]}, Description: {picture[2]}")
    else:
        st.info('No pictures found.')

def add_post():
    st.header('Add Post')

    title = st.text_input('Title', key='add_post_title')
    content = st.text_area('Content', key='add_post_content')

    if st.button('Add Post'):
        cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        st.success('Post added successfully.')

def view_posts():
    st.header('View Posts')

    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    if posts:
        for post in posts:
            st.write(f"Title: {post[1]}\nContent: {post[2]}\n")
    else:
        st.info('No posts found.')

def main():
    if not st.session_state.authenticated:
        admin_login()
    else:
        admin_dashboard()
    
if __name__ == '__main__':
    main()
    # Close the database connection
    conn.close()
