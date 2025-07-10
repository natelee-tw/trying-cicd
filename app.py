import streamlit as st


def get_greeting():
    return "Hello, world! This is a Streamlit app."


def main():
    st.title("Streamlit CI/CD Demo")
    if st.button("Say Hello"):
        st.write(get_greeting())


if __name__ == "__main__":
    main()
