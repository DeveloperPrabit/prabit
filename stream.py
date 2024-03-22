import streamlit as st
from PIL import Image

# Define the data for different programming languages
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
