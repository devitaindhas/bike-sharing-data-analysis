import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
from datetime import datetime


def create_byseason_df(df):
    df = df.groupby(by=['season', 'day_category']).total.sum().unstack()
    df['total_daily_byseason'] = df['Working Day'] + df['Holiday']
    return df

def create_byhour_df(df):
    df = df.groupby(by='hour').agg({
        'casual' : 'sum',
        'registered' : 'sum',
        'total' : ['sum', 'mean']
    })
    df.columns = df.columns.droplevel(1)
    df.columns = ['casual_sum', 'registered_sum', 'total_sum', 'total_mean']
    return df

def create_bymonth_df(df):
    df['month'] = pd.Categorical(df['month'], categories=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
        ordered=True)

    df = df.groupby(by='month').agg({
        'total' : ['sum', 'mean']
    })
    df.sort_values(by='month', ascending=True)
    df.columns = df.columns.droplevel(1)
    df.columns = ['monthly_total', 'monthly_mean']
    return df

day_df = pd.read_csv('https://raw.githubusercontent.com/devitaindhas/bike-sharing-data-analysis/blob/main/dashboard/new_day.csv', index_col=0)
hour_df = pd.read_csv('https:/raw.githubusercontent.com/devitaindhas/bike-sharing-data-analysis/blob/main/dashboard/new_hour.csv',index_col=0)


daily_df = create_byseason_df(day_df)
hourly_df = create_byhour_df(hour_df)
monthly_df = create_bymonth_df(hour_df)


st.title('Analisis Data Sewa Sepeda')

##########################################################
with st.container():
    st.subheader(':sparkles: Tren Sewa Sepeda Harian Berdasarkan Musim', divider='grey')
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Musim dengan Jumlah Sewa Sepeda Tertinggi", value=daily_df['total_daily_byseason'].idxmax())

    with col2:
        st.metric("Hari dengan Sewa Sepeda Tertinggi ", value=daily_df[['Holiday', 'Working Day']].sum().idxmax())

    fig, ax = plt.subplots(figsize=(12,5))

    ax.barh(daily_df.index, daily_df['Working Day'], height=.5, color='darkseagreen', label='Working Day')
    ax.barh(daily_df.index, daily_df['Holiday'], height=.5, color='lightcoral', label='Holiday')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.set_xlabel('Total Sewa', fontsize=18)
    ax.legend(loc='upper right')
    st.pyplot(fig)

##########################################################
with st.container():    
    st.subheader(':sparkles: Tren Sewa Sepeda dari Waktu ke Waktu', divider='grey')

    st.subheader('Berdasarkan Waktu (Dalam 24 Jam)')
    st.metric("Waktu Favorit untuk Bersepeda", value=datetime.strptime(str(hourly_df['total_sum'].idxmax()), '%H').strftime('%H:%M'))

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(hourly_df.index, hourly_df['total_mean'], linestyle='-', color='green')
    
    ax.set_xlabel('Waktu', fontsize=18)
    ax.set_ylabel('Total Sewa Rata-rata', fontsize=18)
    ax.set_xticks(hourly_df.index)
    ax.set_xlim(0, max(hourly_df.index))
    ax.set_ylim(0)

    ax.tick_params(axis='x', which='major', labelsize=12)  
    ax.tick_params(axis='y', which='major', labelsize=8)

    ax.grid(True, alpha=0.5)
    st.pyplot(fig)

    st.write("Jumlah penyewa sepeda yang cukup ramai yaitu pagi hari sekitar pukul 07.00 - 09.00 puncaknya pada pukul 08.00 dan pada sore hari sekitar pukul 16.00 - 18.00 puncaknya adalah pukul 17.00")
#-------------------------------------------------------------------------------#
    st.subheader('Berdasarkan Bulan')
    st.metric("Bulan Favorit Bersepeda", value=monthly_df['monthly_total'].idxmax())

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(monthly_df.index, monthly_df['monthly_mean'], linestyle='-', color='blue')
    plt.xticks(monthly_df.index)
    ax.set_ylabel('Total Sewa Rata-rata', fontsize=18)

    ax.tick_params(axis='x', which='major', labelsize=12)  
    ax.tick_params(axis='y', which='major', labelsize=8)

    ax.grid(True, alpha=0.5)
    st.pyplot(fig)

    st.write("Jumlah penyewa sepeda bervariatif setiap bulan terutama di bulan Juni hingga September. Rata-rata paling banyak di bulan _September_.")

##########################################################
with st.container():    
    st.subheader(':sparkles: Jumlah Sewa Sepeda Berdasarkan Jenis Penyewa', divider='grey')

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 5), gridspec_kw={'width_ratios': [2, 1]})

    ax[0].stackplot(hourly_df.index, hourly_df['casual_sum'], hourly_df['registered_sum'], labels=['Casual', 'Registered'], colors=['skyblue', 'orange'])
    ax[0].set_xticks(hourly_df.index)
    ax[0].set_xlim(0, max(hourly_df.index))
    ax[0].set_ylim(0)
    ax[0].set_title('Casual vs Registered dari Waktu ke Waktu', fontsize=16)
    ax[0].legend()

    sizes = [hour_df['casual'].sum(), hour_df['registered'].sum()]
    labels = ['Casual', 'Registered']
    colors = ['skyblue', 'orange']

    ax[1].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, labeldistance=1.1, pctdistance=0.5)
    ax[1].set_title('Casual vs Registered (%)', fontsize=16)

    plt.tight_layout()

    st.pyplot(fig)

    st.write("Berdasarkan grafik, dapat dilihat bahwa penyewa terbanyak adalah *Penyewa Terdaftar (Registered)*")
