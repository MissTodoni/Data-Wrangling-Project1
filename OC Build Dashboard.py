import pandas as pd 
import streamlit as st 
import plotly.express as px

#-----------Import Data--------------#
#import data
df = pd.read_csv('2025 OC Build Data.csv')


#-------Create Streamlit App-----------#

#create a title
st.title('NWK PE OC Build Dashboard')
st.divider()

#st.dataframe(df)

#-----Data Selector
#grab unique day
Day = df["Date"].unique()
#st.write(Day)

#assign selected day to a variable
day_selected = st.selectbox("Select Day", Day)

#assign selected build type to a variable
#grab unique build type
#BuildType = df["Build Type"].unique()
#build_type_selected = st.selectbox("Select Build Type", df["Build Type"].unique())


#-----Data Filtering
#filter data based on selected week
selected_day_df = df[df["Date"] == day_selected]
#st.dataframe(selected_day_df)
#filter data based on selected Build Type
#selected_Build_Type_df = df[df["Build Type"] == build_type_selected]


#create dataframe with summed sales and count of Store
df_summed = selected_day_df.groupby("Date").agg({"Total": "sum" , "Rejects": "sum", "Yield (%)": "unique", "Build Type": "unique"}).reset_index()
#st.dataframe(df_summed)

#----------Metrics---------------#
#create subheader and columns
st.subheader("Main Metrics", divider='blue')
#create a container to add a border
with st.container(border=True):
    col1, col2, col3 = st.columns(3) 
    # metrics showing: Total OC built, total rejects, yield
    #"${:,.0f}".format()
    col1.metric("Total OC Built", df_summed["Total"].values[0])
    col2.metric("Rejects", df_summed["Rejects"])
    col3.metric("Yield (%)", df_summed["Yield (%)"].values[0])
  

st.header("")  #for spacing purposes  

#-----------Graphs-------------#
#create subheader and tabs
st.subheader("Graphs", divider='red')
tab1, tab2 = st.tabs(["Total Build by Date", "Yield per Day"])

#sum sales by week and Store and build tab1 bar graphs
df_by_Build_Type = selected_day_df.groupby("Build Type")["Total"]. sum().reset_index()
#st.dataframe(df_by_Store)
with tab1:
        fig = px.bar(df_by_Build_Type, x = "Build Type" , y = "Total", title= "Total OC Build by Build Type")
        st.plotly_chart(fig, use_container_width= True)

with tab2:
        fig = px.line(df, x = "Date" , y = "Yield (%)", title= "Yield by Date")
        st.plotly_chart(fig, use_container_width= True)