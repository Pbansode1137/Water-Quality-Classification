import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open("/content/trained_model.sav","rb"))

#loadiing the scaler object
loaded_scaler = pickle.load(open("/content/scaler.pkl","rb"))

def water_prediction(input_data):
    input_data = np.asarray(input_data)
    # we need to reshape the array as we are passing for single instance
    input_data_reshape = input_data.reshape(1,-1)
    x_test_scaling = loaded_scaler.transform(input_data_reshape)
    prediction = loaded_model.predict(x_test_scaling)
    y_pred = np.where(prediction>0.5,1,0)

    
    if (y_pred[0][0]==0):
        print("The water quality is not safe for drinking")
    else:
        print("The water quality is safe for drinking")
def main():
    # giving the title to the web page
    st.title("To find the water is safe for drinking or not")
    # getting the input from the web page
    aluminium = st.text_input("content of aluminium")
    ammonia = st.text_input("content of ammonia")
    arsenic = st.text_input("content of arsenic")
    barium = st.text_input("content of barium")
    cadmium = st.text_input("content of cadmium")
    chloramine = st.text_input("content of chloramine")
    chromium = st.text_input("content of chromium")
    copper = st.text_input("content of copper")
    flouride = st.text_input("content of flouride")
    bacteria = st.text_input("content of bacteria")
    viruses = st.text_input("content of viruses")
    lead = st.text_input("content of lead")
    nitrates = st.text_input("content of nitrates")
    nitrites = st.text_input("content of nitrites")
    mercury = st.text_input("content of mercury")
    perchlorate = st.text_input("content of perchlorate")
    radium = st.text_input("content of radium")
    selenium = st.text_input("content of selenium")
    silver = st.text_input("content of silver")
    uranium = st.text_input("content of uranium")

    # code for the prediction
    Quality = ""
    
    # creating the button for prediction
    if st.button("Water Test Result"):
        Quality = water_prediction([aluminium,ammonia,arsenic,barium,cadmium,chloramine,chromium,copper,flouride,bacteria,viruses,lead,nitrates,nitrites,mercury,perchlorate,radium,selenium,silver,uranium])
    st.success(Quality)
if __name__=='__main__':
    main()
