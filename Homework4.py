
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#Question 1 
st.title("Week 4 Homework")
#Question 2
st.markdown("[Remi Inoue](https://github.com/remii11/Math-10)")
#Question 3
uploaded_file= st.file_uploader(label ="Upload a CSV File",type="CSV")
#Question 4
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
#Question 5
    #if x is an empty string, make it numpy's not a number
    #otherwise leave x alone
    df = df.applymap(lambda x: np.nan if x == " " else x)     
#Question 6
    def can_be_numeric(c):
        try :
            pd.to_numeric(df[c])
            return True
        except :
            return False
    good_cols = [c for c in df.columns if can_be_numeric(c)]
#Question 7
    df[good_cols]=df[good_cols].apply(pd.to_numeric,axis = 0)
#Question 8
    x_axis =st.selectbox('Choose an x-value',good_cols)
    y_axis =st.selectbox('Choose a y-value',good_cols)
#Question 9
    select_range = st.slider(label = "Choose the number of rows to plot",value = (0,len(df)-1))
    df = df[select_range[0]:select_range[1]]
#Question 12
    select_color = st.radio("Select a color",("Blue","Green","Red","Pink","Purple"))
#Question 10
    st.write(f"{x_axis} is displayed as the x-axis and {y_axis} is displayed as the y-axis")
    st.write(f"Rows {select_range[0]} through {select_range[1]} are displayed")
#Question 11
    st.altair_chart(alt.Chart(df).mark_circle(
        fill = select_color
        ).encode(
        x = x_axis,
        y = y_axis,
        ))
st.write(st.__version__)
st.write(np.__version__)
st.write(pd.__version__)
st.write(alt.__version__)
    
        
    
