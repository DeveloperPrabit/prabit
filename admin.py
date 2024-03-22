import streamlit as st
import sqlite3

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
                admin_dashboard()
            else:
                st.error('You do not have admin privileges.')
        else:
            st.error('Invalid username or password.')

def admin_dashboard():
    st.title('Admin Dashboard')

    # Sidebar options
    selected_option = st.sidebar.radio(
        'Admin Options',
        ['Add User', 'Remove User', 'Edit User', 'View Users', 'Add Picture', 'View Pictures', 'Add Post', 'View Posts', 'Exit'],
        key='admin_options_radio'  # Unique key for the radio group
    )

    # Generate unique keys based on selected option
    add_user_key = 'add_user' if selected_option == 'Add User' else None
    remove_user_key = 'remove_user' if selected_option == 'Remove User' else None
    edit_user_key = 'edit_user' if selected_option == 'Edit User' else None
    view_users_key = 'view_users' if selected_option == 'View Users' else None
    add_picture_key = 'add_picture' if selected_option == 'Add Picture' else None
    view_pictures_key = 'view_pictures' if selected_option == 'View Pictures' else None
    add_post_key = 'add_post' if selected_option == 'Add Post' else None
    view_posts_key = 'view_posts' if selected_option == 'View Posts' else None

    if selected_option == 'Add User':
        add_user(add_user_key)
    elif selected_option == 'Remove User':
        remove_user(remove_user_key)
    elif selected_option == 'Edit User':
        edit_user(edit_user_key)
    elif selected_option == 'View Users':
        view_users(view_users_key)
    elif selected_option == 'Add Picture':
        add_picture(add_picture_key)
    elif selected_option == 'View Pictures':
        view_pictures(view_pictures_key)
    elif selected_option == 'Add Post':
        add_post(add_post_key)
    elif selected_option == 'View Posts':
        view_posts(view_posts_key)
    elif selected_option == 'Exit':
        st.stop()

def add_user(key=None):
    st.header('Add User')

    username = st.text_input('Username', key='add_user_username')
    email = st.text_input('Email', key='add_user_email')
    password = st.text_input('Password', type='password', key='add_user_password')
    is_admin = st.checkbox('Admin Privileges', key='add_user_checkbox')

    if st.button('Add User', key=key):
        try:
            cursor.execute("INSERT INTO users (username, email, password, is_admin) VALUES (?, ?, ?, ?)",
                           (username, email, password, 1 if is_admin else 0))
            conn.commit()
            st.success('User added successfully.')
        except sqlite3.IntegrityError:
            st.error('Username or email already exists.')

def remove_user(key=None):
    st.header('Remove User')

    username = st.text_input('Username', key='remove_user_username')

    if st.button('Remove User', key=key):
        cursor.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
        st.success('User removed successfully.')

def edit_user(key=None):
    st.header('Edit User')

    username = st.text_input('Username', key='edit_user_username')
    email = st.text_input('Email', key='edit_user_email')
    password = st.text_input('Password', type='password', key='edit_user_password')
    is_admin = st.checkbox('Admin Privileges', key='edit_user_checkbox')

    if st.button('Update User', key=key):
        cursor.execute("UPDATE users SET email=?, password=?, is_admin=? WHERE username=?",
                       (email, password, 1 if is_admin else 0, username))
        conn.commit()
        st.success('User updated successfully.')

def view_users(key=None):
    st.header('View Users')

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    if users:
        for user in users:
            st.write(f"Username: {user[1]}, Email: {user[2]}, Admin: {'Yes' if user[4] == 1 else 'No'}")
    else:
        st.info('No users found.')

def add_picture(key=None):
    st.header('Add Picture')

    filename = st.text_input('Filename', key='add_picture_filename')
    description = st.text_input('Description', key='add_picture_description')

    if st.button('Add Picture', key=key):
        try:
            cursor.execute("INSERT INTO pictures (filename, description) VALUES (?, ?)", (filename, description))
            conn.commit()
            st.success('Picture added successfully.')
        except sqlite3.IntegrityError:
            st.error('Filename already exists.')

def view_pictures(key=None):
    st.header('View Pictures')

    cursor.execute("SELECT * FROM pictures")
    pictures = cursor.fetchall()

    if pictures:
        for picture in pictures:
            st.write(f"Filename: {picture[1]}, Description: {picture[2]}")
    else:
        st.info('No pictures found.')

def add_post(key=None):
    st.header('Add Post')

    title = st.text_input('Title', key='add_post_title')
    content = st.text_area('Content', key='add_post_content')

    if st.button('Add Post', key=key):
        cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        st.success('Post added successfully.')

def view_posts(key=None):
    st.header('View Posts')

    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    if posts:
        for post in posts:
            st.write(f"Title: {post[1]}\nContent: {post[2]}\n")
    else:
        st.info('No posts found.')

def main():
    admin_login()
    
if __name__ == '__main__':
    main()
