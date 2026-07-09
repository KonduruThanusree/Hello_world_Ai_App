import streamlit as st
import numpy as np
from model import train

#title
st.title("Hello world AI App")
st.subheader("A simple regression model")

#train model
model=train()

#sidebar
st.sidebar.header("input features")
input_value=st.sidebar.slider("select value f x",1,10,1)

input_array=np.array([[input_value]])
Prediction=model.predict(input_array)

#display result
st.write(f'### Input value:{input_value}')
st.write(f'### Output value:{Prediction[0]:.2f}')