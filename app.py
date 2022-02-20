import streamlit as st
import joblib
model = joblib.load('car')
st.title('FRONT OR REAR')            
ip = st.text_input('Enter the name of the car ')       
op = model.predict([ip])           
if st.button('click'):   
  st.title(op[0]) 
        
