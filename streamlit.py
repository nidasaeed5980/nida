import pandas as pd
import numpy as np
import time
import plotly.express as px
import streamlit as st
a=st.sidebar.selectbox("select box",['a','b',"c"])
if a=="a":
    st.title("my dashboard")
    st.header("nida")
    st.subheader("abc")
    st.write("welcome😍😍")
    st.image("abcd.jFIF")
    st.radio('what is your favourite game',["cricket","basketball"])
    st.selectbox("your dashboard",["abc","def"])
    st.multiselect("your dashboard😍😍",["abc","def"])
elif a=="b":
    text=st.text_area("enter text")
    st.write(text)
    num=st.number_input("enter a number",min_value=0,max_value=10)
    st.write(num)
    file=st.file_uploader("select file",type="csv")
    if file:
        st.write("file upladed 😍")
    st.slider("select your range",0,10)
elif a=="c":
    button=st.button("nida")
    if button:
        st.write("work done")
    st.sidebar.header("abc")
    z=st.sidebar.selectbox("select box",["abc","def"])
    if z=="abc":
        st.title("hyy")
    elif z=="def":
        st.title("welcom")

df=pd.DataFrame({
    'a':np.arange(10),
    "b":np.random.randn(10)
})
st.table(df)
fig=px.line(df,x='a',y='b',title='line plot')
st.plotly_chart(fig)
fig1=px.scatter(df,x="a",y="b",title="scatter plot")
st.plotly_chart(fig1)


