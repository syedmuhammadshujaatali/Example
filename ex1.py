import streamlit as st

def quiz():
    st.title("Quiz Game")

    score = 0

    questions = [
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

    num_questions = len(questions)

    for i, (question, answer) in enumerate(questions):
        st.subheader(f"Question {i+1}:")
        st.write(question)
        user_answer = st.text_input("Your Answer:")

        if user_answer.lower() == answer.lower():
            st.write("Correct!")
            score += 1
        else:
            st.write(f"Incorrect! The correct answer is: {answer}")

    st.write(f"Your final score is: {score}/{num_questions}")

    if st.button("Play Again"):
        quiz()

def main():
    st.sidebar.title("Navigation")
    st.sidebar.markdown("""
        <div style="display: flex; justify-content: center;">
            <img src="https://banoqabil.pk/media/logo.png" width="200">
        </div>
    """)
    tab = st.sidebar.radio("", ["Quiz", "About us", "Contact us"])

    if tab == "Quiz":
        quiz()
    elif tab == "About us":
        st.title("About Us Page")
        st.write("Welcome to our About Us Page. Here, you can learn about our company and its history.")
        # Add content for the about us page here
    elif tab == "Contact us":
        st.title("Contact Us Page")
        st.write("Welcome to our Contact Us Page. You can reach out to us using the contact information provided.")
        # Add content for the contact us page here

if __name__ == "__main__":
    main()
