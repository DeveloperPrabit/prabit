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
    selected_option = st.sidebar.radio('Admin Options', ['Add User', 'Remove User', 'Add Picture', 'Remove Picture', 'Add Post', 'Remove Post'])

    if selected_option == 'Add User':
        add_user()
    elif selected_option == 'Remove User':
        remove_user()
    elif selected_option == 'Add Picture':
        add_picture()
    elif selected_option == 'Remove Picture':
        remove_picture()
    elif selected_option == 'Add Post':
        add_post()
    elif selected_option == 'Remove Post':
        remove_post()


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


def remove_picture():
    st.header('Remove Picture')

    filename = st.text_input('Filename', key='remove_picture_filename')

    if st.button('Remove Picture'):
        cursor.execute("DELETE FROM pictures WHERE filename=?", (filename,))
        conn.commit()
        st.success('Picture removed successfully.')


def add_post():
    st.header('Add Post')

    title = st.text_input('Title', key='add_post_title')
    content = st.text_area('Content', key='add_post_content')

    if st.button('Add Post'):
        cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        st.success('Post added successfully.')


def remove_post():
    st.header('Remove Post')

    post_id = st.number_input('Post ID', min_value=1, key='remove_post_id')

    if st.button('Remove Post'):
        cursor.execute("DELETE FROM posts WHERE id=?", (post_id,))
        conn.commit()
        st.success('Post removed successfully.')


def main():
    admin_login()


if __name__ == '__main__':
    main()
