import streamlit as st
import pickle
import numpy as np




page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background: rgb(238, 223, 199);
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.header(':red[Diabetes Prediction 🩺💊]')
option1 = st.radio('**Select your Gender**',('Female', 'Male','Others'),horizontal=True)
if option1 == 'Female':
    gender = 0
elif option1 == 'Male':
    gender = 1
elif option1 == 'Others':
    gender = 2

age = st.number_input('**Enter your age**', min_value=0, max_value=120, value= 25)

option2 = st.radio('**Are you having Hypertension?**',('Yes','No'),horizontal=True)
if option2 == 'Yes':
    hp = 1
elif option2 == 'No':
    hp = 0

option3 = st.radio('**Are you having Heart Disease?**',('Yes','No'),horizontal=True)
if option3 == 'Yes':
    hd = 1
elif option3 == 'No':
    hd = 0

option4 = st.selectbox("**Select your Smoking History**",["Never",
                                                          "No Information",
                                                          "Current",
                                                          "Former",
                                                          "Ever",
                                                          "Not Current"])

if option4 == "Never":
    smoke = 4.0
elif option4 == "No Information":
    smoke = 0.0

elif option4 == "Current":
    smoke =1.0
    
elif option4 == "Former":
    smoke =3.0

elif option4 == "Ever":
    smoke =2.0

elif option4 == "Not Current":
    smoke =5.0

Bmi = st.number_input('**Enter your BMI Value**', min_value=0.0, max_value=100.0, value= 18.0)

hb_level = st.number_input('**Enter your HbA1c level**', min_value=0.0, max_value=10.0, value= 4.0)

gl_level = st.number_input('**Enter your blood glucose level**', min_value=50, max_value=500, value=150)

st.markdown("""
    <style>
    div.stButton > button {
        background-color: green;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

if st.button('Calculate'):
    file_path="C:/Users/siva Bharathi/OneDrive/Desktop/Python/diabetes_result"
    diab = pickle.load(open(file_path,'rb'))
    input_data = np.array([[gender, age, hp, hd, smoke, Bmi, hb_level, gl_level]])
    result = diab.predict(input_data)
    if result[0] == 0:
        st.success("🎉Congrats! You don't have diabetes")
    else:
        st.success("😢oops!, You have diabetes")
