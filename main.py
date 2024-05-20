import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Cab Industry Dashboard', page_icon=':bar_chart:', layout='wide')

df = pd.read_csv('./genderdata.csv')

#Setting Sidebar with streamlit 

st.sidebar.header('Please Filter Here:')

gender = st.sidebar.multiselect('Select the Gender:',
                              options=df['gender'].unique())

username = st.sidebar.multiselect('Select the Username:',options=df['username'].unique())

# Creating query selection to build a dataFrame based on the selection

df_selector = df.query(
    'gender == @gender and username == @username'
)

#setting the ----Main Page --- of the steamlit app

st.title("bar_chart: Male and Female Table")
st.markdown('##')

#Setting the TOP KPI(Key Point  Identification)

total_gender = df.gender.count()
total_male =  df[df.gender == 'Male'].count()
total_female = df[df.gender == 'Female'].count()

# Making the interactive totals
interactive_total = df_selector['gender'].count()

#Defining the columns to Display your KPIs

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Total Gender:')
    st.subheader(f'{interactive_total} Persons')

with middle_column:
    st.subheader('Total Male Gender')
    st.subheader(f'{total_male.gender} Males')

with right_column:
    st.subheader('Total Female Gender')
    st.subheader(f'{total_female.gender} Females')

# Seperate the KPI from other section by bringing in the markdown method

st.markdown('---')

gender_by_gender = (df_selector.groupby(by=['gender']).count())

print(gender_by_gender)
print(df_selector)

#Plot gender bar chart

# gender_line = (
#     df.groupby(by=['gender']).sum()[["Total"]]
#
# )

fig_gender = px.bar(
    gender_by_gender,
    x= 'username',
    y = gender_by_gender.index,
    orientation='h',
    title='<b>Gender by Total</b>',
    color_discrete_sequence=['blue '] * len(gender_by_gender),
    template='plotly_white'
)
#
st.plotly_chart(fig_gender)
st.dataframe(df_selector)