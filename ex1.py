import streamlit as st
import random

st.title("Bano Qabil 2.0")

# Display the Bano Qabil logo
st.sidebar.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://banoqabil.pk/media/logo.png" width="200">
    </div>
""", unsafe_allow_html=True)  # Allow HTML rendering in Streamlit

# List of scrambled sentences
sentences = [
     ("What does GB stand for in computing?", "Gigabyte"),
    ("When was the first computer invented?", "Various"),
    ("What does CPU stand for?", "Central Processing Unit"),
    ("What component produces audio output on a computer?", "Speaker"),
    ("What is needed to connect to the internet?", "Device"),
    ("What does WWW stand for?", "World Wide Web"),
    ("What do the initials CD stand for?", "Compact Disc"),
    ("Who invented the first mechanical computer?", "Babbage"),
    ("What does a Printer do?", "Printing"),
    ("What does bit stand for in computing?", "Binary")
]

# Function to scramble the words in a sentence
def scramble_sentence(sentence):
    words = sentence.split()
    random.shuffle(words)
    return " ".join(words)

# Function to check if the user's answer is correct
def check_answer(original_sentence, user_answer):
    return original_sentence == user_answer

def main():
    st.sidebar.title("Navigation")
    tab == st.sidebar.radio("", ["Home", "About us", "Contact us"])

 if tab == "Home":
        st.title("Puzzle Game")

    # Select a random sentence from the list
    sentence = random.choice(sentences)
    scrambled_sentence = scramble_sentence(sentence)

    st.write("Unscramble the sentence:")
    st.write(scrambled_sentence)

    user_answer = st.text_input("Your Answer")

    if st.button("Check Answer"):
        if check_answer(sentence, user_answer):
            st.success("Congratulations! Your answer is correct.")
        else:
            st.error("Sorry, your answer is incorrect. Please try again.")

elif tab == "About us":
        st.title("About Us")
        st.markdown(
            """
            **Team Name**: Python Programmer  
            **Team Leader**: Syed Muhammad Shujaat Ali  
            **Members**:  
            - Hafiz M. Abdul Rehman  
            - Muhammad Anus  

            **Project Description**:  
            The final project submitted in Bano Qabil 2.0.  
            This project is a puzzle game developed using Python. Puzzle games are excellent for learning and help in developing crucial skills like problem-solving and critical thinking. This game is built online and provides an engaging platform for users to enhance their cognitive abilities.
            """
        )
    elif tab == "Contact us":
        st.title("Contact Us")
        st.markdown(
            """
            **Leader**: Syed Muhammad Shujaat Ali  
            **Email**: shujaatali@gmail.com  
            **Contact**: 03321031301  

            **Member2: Muhammad Anus**  
            **Email**: anusmahir6@gmail.com  
            **Contact**: 03162785597  

            **Member3: Hafiz M. Abdul Rehman**  
            **Email**: chappalwala00@gmail.com  
            **Contact**: 03162343374  
            """
        )

if __name__ == "__main__":
    main()
