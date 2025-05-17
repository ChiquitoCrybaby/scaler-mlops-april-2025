import streamlit as st
import pickle
import joblib

st.write("Car prediction analysis")

encode_dict = {
    "Fuel":  {"PETROL": 1, "DIESEL": 2, "CNG": 3, "LPG": 4},
    "Drive": {"Manual": 0,  "Automatic": 1}
}

model = joblib.load("cars_24_combined.joblib")

year = st.slider("Manufacturing Year", min_value = 1998, max_value = 2024, value = 2015, step = 1)
distance = st.slider("Distance on meter", min_value = 15000, max_value = 150000, value = 5000,step =5000)
owner = st.selectbox("Owner Type",['1st Owner','2nd Owner','3rd owner', '4th Owner'])
Fuel = st.slider("Fuel Type", min_value = 1, max_value =4, value = 1, step =1)
Drive = st.selectbox("Gear Type",['Manual','Automatic'])

scaler = joblib.load('scaler.pkl')

def model_predict(
        year,distance,owner,Fuel,Drive
):
    
    drive_type_encode = encode_dict['Drive'][Drive]


    data = [[float(year), float(distance),float(owner),float(Fuel), float(Drive)]]

    data = scaler.transform(data)

    prediction = model.predict(data)
    return round(prediction[0],2)

if st.button("Predict"):
    price = model_predict(year,distance,owner,Fuel,Drive)
    st.write(f"Predict car prices :{price}")
else:
    st.write("click on the predict button")
