import streamlit as st

st.title("Aradhy's Page")
st.header("Demo")
data=st.text_input("Enter your choice as + - / *:")

if data:
    a=int(st.text_input("Enter first number:", placeholder=2, value=0))
    b=int(st.text_input("Enter secod number:", placeholder=3, value=0))
    if data=="+":
        st.write(a+b)
    elif data=="-":
        st.write(a-b)
    elif data=="*":
        st.write(a*b)
    elif data=="/":
        if a>=b:
            st.write(a/b)
    else:
        st.write("Wrong entry in operation!")
else:
    st.write("Enter the operations!")
        