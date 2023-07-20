# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 22:12:35 2023

@author: Mayur
"""
import pickle
import streamlit as st

st.title('Predict customer segmentation! :chart:')

load = open('model.pkl','rb')
model = pickle.load(load)


def predict(income,recency,customer_age,total_purcheses):
    prediction = model.predict([[income,recency,customer_age,total_purcheses]])
    return prediction

def main():
    
    st.markdown('This is a very simple webapp for customer segmentation! :chart:')
    income = st.number_input('Income')
    recency = st.number_input('Recency',min_value = 0 , max_value = 100)
    customer_age = st.number_input('Customer_Age', min_value = 0 , max_value = 100)
    total_purcheses = st.number_input('Total_purcheses',min_value = 0 , max_value = 100)
    if st.button('Predict'):
        result = predict(income,recency,customer_age,total_purcheses)
        st.success('Customer Segment:{} '.format(result))
        
if __name__ == '__main__':
    main()
        
         