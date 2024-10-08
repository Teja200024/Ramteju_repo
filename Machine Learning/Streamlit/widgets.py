import streamlit as st

st.title("My favorite Programming language ")

name = st.text_input("Enter your Name:")


if name:
    st.write(f"Hello {name}")

age=st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}.")


options = ["Select","Python","Go","C++","JS"]
choice = st.selectbox("Choose your favorite Programming language",options)
if choice =="Python":
    st.write(f"Excellent Choice {name} , you have selected {choice}. It is a best programming language ,to learn various things mainly used by DS.")
elif choice =="Go":
    st.write(f"Great Choice {name} , you have selected {choice}. It is a good programming language ,mainly used by Devops Engineer.")
elif choice =='C++' or choice=='JS':
    st.write(f"Super Choice {name} , you have selected {choice}. It is a good programming language ,Happy Learning")





