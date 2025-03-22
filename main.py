import streamlit as st
import pickle

st.subheader('Taxi Uber Ride Prediction')
ppw=st.number_input('Enter 	Priceperweek')
pop=st.number_input('Enter Population')
mntin=st.number_input('Enter Monthlyincome')
appm=st.number_input('Enter Averageparkingpermonth')
button=st.button('Predict!')


if button:
    model=pickle.load(open('taxi.pkl','rb'))
   
    res=model.predict([[ppw,pop,mntin,appm]])[0]
    st.markdown(f'''
   Number Of Weakly Riders:{res}
                ''')