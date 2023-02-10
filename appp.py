import pandas as pd
import streamlit as st 
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pickle import dump
from pickle import load
import warnings
warnings.filterwarnings('ignore')




st.title('Model Deployment: Time Serise Forcasting')
st.sidebar.header('User Input Period Of Forcasting')
# def user_input_features():
#     Start_Date = st.sidebar.date_input("Enter Start Date For Prediction")
#     End_Date = st.sidebar.date_input("Enter Start End For Prediction")
#     data = {'Start_Date':Start_Date,
#             'End_Date':End_Date}
#     
#     features = pd.DataFrame(data,index = [0])
#     return features 
#     
# df = user_input_features()
# st.subheader('User Input For Stock Prediction')
# st.write(df)
Stock_df = load(open('model_trained.sav', 'rb'))
    

Days_pred = st.number_input('Number of Days',min_value=1)

datetime = pd.date_range('2020-01-01', periods=Days_pred,freq='B')
date_df = pd.DataFrame(datetime,columns=['Date'])
model_sarima_final = model_SA =sm.tsa.SARIMAX(['Close'],order=(0,1,2),seasonal_order=(1,1,0,57))
sarima_fit_final = model_SA_final.fit()
forecast_SA=result_SA.predict(len(df),len(df)+31,type='levels')
forecast_SA
index_future_dates=pd.date_range(start='2019-12-30',end='2020-01-30')
forecast_SA.index=index_future_dates
st.subheader('Predicted Price For Stock')
data_forecast = forecast_df.set_index(date_df.Date)
st.success('Forecasting stock price value for '+str(Days_pred)+' days')
st.write(data_forecast)

st.subheader('Graphical Presentation Of Predicted Price')
fig,ax = plt.subplots(figsize=(16,8),dpi=100)
ax.plot(Stock_df, label='Actual')
ax.plot(data_forecast,label='Forecast')
ax.set_title('Apple Stock Forecast')
ax.set_xlabel('Date')
ax.set_ylabel('Stock Price')
ax.legend(loc='upper left',fontsize=12)
ax.grid(True)
st.pyplot(fig)
