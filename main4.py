
import streamlit as st
import pickle
st.subheader('Weather Prediction..')
pn=st.number_input('Enter Precipation')
maxt=st.number_input('Enter Maximum Temperature')
mint=st.number_input('Enter Minimum Temperature')
wind=st.number_input('Enter Wind Speed')
button=st.button('Predict!')


if button:
    model=pickle.load(open('wp.pkl','rb'))
   
    res=model.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f'''
    Weather Condition:{res}
                ''')


