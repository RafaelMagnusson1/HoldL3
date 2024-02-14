import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import matplotlib as plt
import numpy as np

TEs_31= ['BB04631TE007 (°C)', 'BB04631TE008 (°C)', 'BB04631TE009 (°C)',
       'BB04631TE010 (°C)', 'BB04631TE011 (°C)', 'BB04631TE012 (°C)',
       'BB04631TE013 (°C)', 'BB04631TE014 (°C)', 'BB04631TE015 (°C)',
       'BB04631TE016 (ºC)', 'BB04631TE018 (°C)', 'BB04631TE019 (°C)',
       'BB04631TE020 (°C)', 'BB04631TE022 (°C)', 'BB04631TE023 (ºC)',
       'BB04631TE024 (°C)', 'BB04631TE025 (°C)', 'BB04631TE026 (°C)',
       'BB04631TE027 (°C)']


TEs_32 = ['BB04632TE006 (°C)', 'BB04632TE007 (°C)', 'BB04632TE008 (°C)',
       'BB04632TE009 (°C)', 'BB04632TE010 (°C)',
       'BB04632TE012 (°C)', 'BB04632TE013 (°C)', 'BB04632TE014 (°C)',
       'BB04632TE015 (°C)', 'BB04632TE017 (°C)', 'BB04632TE018 (°C)',
       'BB04632TE025 (°C)', 'BB04632TE026 (°C)', 'BB04632TE027 (°C)',
       'BB04632TE049 (°C)']

TEs_33 = ['BB04633TE006 (°C)',
       'BB04633TE007 (°C)', 'BB04633TE008 (°C)', 'BB04633TE009 (°C)',
       'BB04633TE010 (°C)', 'BB04633TE011 (°C)', 'BB04633TE012 (°C)',
       'BB04633TE013 (°C)', 'BB04633TE014 (°C)', 'BB04633TE015 (°C)',
       'BB04633TE017 (°C)', 'BB04633TE018 (°C)', 'BB04633TE019 (°C)',
       'BB04633TE020 (°C)', 'BB04633TE021 (°C)', 'BB04633TE024 (°C)',
       'BB04633TE025 (°C)', 'BB04633TE027 (°C)']



st.set_page_config(page_title = "Dashboard Amyris - Sterility Hold L3")
st.title("Dashboard - Sterility hold L3")

uploaded_file_MF = st.file_uploader("Upload do arquivo de barreira de vapor dos MFs")
uploaded_file_SF = st.file_uploader("Upload do arquivo de barreira de vapor dos SFs")

if uploaded_file_MF is not None:
    
    bytes_data = uploaded_file_MF.getvalue()
    df_MF = pd.read_csv(uploaded_file_MF)
    df_MF['Time'] = pd.to_datetime(df_MF['Time']).dt.floor('S')
    df_MF.set_index('Time', inplace=True)

else:

    df_vazio_MF = pd.DataFrame(columns=['BB04632TE006 (°C)', 'BB04632TE007 (°C)', 'BB04632TE008 (°C)',
       'BB04632TE009 (°C)', 'BB04632TE010 (°C)', 'BB04632TE011 (°C)',
       'BB04632TE012 (°C)', 'BB04632TE013 (°C)', 'BB04632TE014 (°C)',
       'BB04632TE015 (°C)', 'BB04632TE017 (°C)', 'BB04632TE018 (°C)',
       'BB04632TE023 (ºC)', 'BB04632TE025 (°C)', 'BB04632TE026 (°C)',
       'BB04632TE027 (°C)', 'BB04632TE049 (°C)', 'BB04633TE006 (°C)',
       'BB04633TE007 (°C)', 'BB04633TE008 (°C)', 'BB04633TE009 (°C)',
       'BB04633TE010 (°C)', 'BB04633TE011 (°C)', 'BB04633TE012 (°C)',
       'BB04633TE013 (°C)', 'BB04633TE014 (°C)', 'BB04633TE015 (°C)',
       'BB04633TE017 (°C)', 'BB04633TE018 (°C)', 'BB04633TE019 (°C)',
       'BB04633TE020 (°C)', 'BB04633TE021 (°C)', 'BB04633TE024 (°C)',
       'BB04633TE025 (°C)', 'BB04633TE027 (°C)', 'BB04633TE029 (°C)'])
    df_MF = df_vazio_MF.copy()

if uploaded_file_SF is not None:
    
    bytes_data = uploaded_file_SF.getvalue()
    df_SF = pd.read_csv(uploaded_file_SF)
    df_SF['Time'] = pd.to_datetime(df_SF['Time']).dt.floor('S')
    df_SF.set_index('Time', inplace=True)

else:

    df_vazio_SF = pd.DataFrame(columns=['BB04631TE007 (°C)', 'BB04631TE008 (°C)', 'BB04631TE009 (°C)',
       'BB04631TE010 (°C)', 'BB04631TE011 (°C)', 'BB04631TE012 (°C)',
       'BB04631TE013 (°C)', 'BB04631TE014 (°C)', 'BB04631TE015 (°C)',
       'BB04631TE016 (ºC)', 'BB04631TE018 (°C)', 'BB04631TE019 (°C)',
       'BB04631TE020 (°C)', 'BB04631TE022 (°C)', 'BB04631TE023 (ºC)',
       'BB04631TE024 (°C)', 'BB04631TE025 (°C)', 'BB04631TE026 (°C)',
       'BB04631TE027 (°C)'])
    
    df_SF = df_vazio_SF.copy()




mean_32=[]
for i in df_MF[TEs_32].columns:
    mean_32.append(df_MF[TEs_32][i].mean())
    
std_32=[]
for i in df_MF[TEs_32].columns:
    std_32.append(df_MF[TEs_32][i].std())


mean_33=[]
for i in df_MF[TEs_33].columns:
    mean_33.append(df_MF[TEs_33][i].mean())
    
std_33=[]
for i in df_MF[TEs_33].columns:
    std_33.append(df_MF[TEs_33][i].std())

coluna1, coluna2,coluna3 = st.columns(3)

with coluna1:
    
    #Barreiras de vapor do SF 3.1

    today = datetime.datetime.now()
    jan_1 = datetime.date(today.year, 1, 1)
        
    d_31 = st.date_input("Data TEs 3.1",(jan_1, today) , format="DD/MM/YYYY")

    data_inicial, data_final = pd.to_datetime(d_31)

    df_filt_31 = df_SF[TEs_31].loc[(df_SF[TEs_31].index >= data_inicial) & (df_SF[TEs_31].index <= data_final)]

    mean_31_f=[]
    for i in df_filt_31.columns:
        mean_31_f.append(df_filt_31[i].mean())
    
    std_31_f=[]
    for i in df_filt_31.columns:
        std_31_f.append(df_filt_31[i].std())


        #Plotando os gráficos:

    fig31_f = px.bar(x=TEs_31, y=mean_31_f, error_y= std_31_f, title='Média de temperatura (ºC) do SF',
             labels={'x': 'Skin points', 'y': 'Média de temperatura (ºC)'}, color_discrete_sequence=['purple'])
    fig31_f.update_yaxes(range=[0, 150])

    st.plotly_chart(fig31_f)


with coluna2:
    
    #Barreiras de vapor do MF 3.2

    today = datetime.datetime.now()
    jan_1 = datetime.date(today.year, 1, 1)
        
    d_32 = st.date_input("Data TEs 3.2",(jan_1, today) , format="DD/MM/YYYY")


    data_inicial, data_final = pd.to_datetime(d_32)

    df_filt_32 = df_MF[TEs_32].loc[(df_MF[TEs_32].index >= data_inicial) & (df_MF[TEs_32].index <= data_final)]

    mean_32_f=[]
    for i in df_filt_32.columns:
        mean_32_f.append(df_filt_32[i].mean())
    
    std_32_f=[]
    for i in df_filt_32.columns:
        std_32_f.append(df_filt_32[i].std())


        #Plotando os gráficos:

    fig32_f = px.bar(x=TEs_32, y=mean_32_f, error_y= std_32_f, title='Média de temperatura (ºC) do MF 3.2',
             labels={'x': 'Skin points', 'y': 'Média de temperatura (ºC)'}, color_discrete_sequence=['purple'])
    fig32_f.update_yaxes(range=[0, 150])

    st.plotly_chart(fig32_f)


    
with coluna3:
    
    #Barreiras de vapor do MF 3.3

    today = datetime.datetime.now()
    jan_1 = datetime.date(today.year, 1, 1)
        
    d_33 = st.date_input("Data TEs 3.3",(jan_1, today) , format="DD/MM/YYYY")


    data_inicial, data_final = pd.to_datetime(d_33)

    df_filt_33 = df_MF[TEs_33].loc[(df_MF[TEs_33].index >= data_inicial) & (df_MF[TEs_33].index <= data_final)]

    mean_33_f=[]
    for i in df_filt_33.columns:
        mean_33_f.append(df_filt_33[i].mean())
   
    std_33_f=[]
    for i in df_filt_33.columns:
        std_33_f.append(df_filt_33[i].std())
    

        #Plotando os gráficos:

    fig33_f = px.bar(x=TEs_33, y=mean_33_f, error_y= std_33_f, title='Média de temperatura (ºC) do MF 3.3',
             labels={'x': 'Skin points', 'y': 'Média de temperatura (ºC)'}, color_discrete_sequence=['purple'])
    fig33_f.update_yaxes(range=[0, 150])

    st.plotly_chart(fig33_f)