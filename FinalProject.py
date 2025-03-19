#-----------Import Packages----------#
import pandas as pd 
import streamlit as st 
import plotly.express as px

#-----------Import Data--------------#
#import data
df = pd.read_csv('Walmart_Sales.csv')

#-----------Initial Data Wrangling----------------#
#transform date to a datetime
df["Date"] = pd.to_datetime(df["Date"], format='%d-%m-%Y')

#date truncing to the week for comparisons and create as new column
df["Date"] = df["Date"].dt.to_period('W').dt.to_timestamp().dt.date


#-------Create Streamlit App-----------#

#create a title
st.title('Walmart Stores Weekly Sales Dashboard')
st.divider()

#st.dataframe(df)

#-----Data Selector
#grab unique week
weeks = df["Date"].unique()
#st.write(weeks)

#assign selected week to a variable
week_selected = st.selectbox("Select Week", weeks)

#-----Data Filtering
#filter data based on selected week
selected_week_df = df[df["Date"] == week_selected]
#st.dataframe(selected_week_df)


#create dataframe with summed sales and count of Store
df_summed = selected_week_df.groupby("Date").agg({"Weekly_Sales": "sum" , "Store": "nunique"}).reset_index()
df_summed["AvgWeekly_Sales"] = round(df_summed["Weekly_Sales"] / df_summed["Store"], 0)
#st.dataframe(df_summed)



#----------Metrics---------------#
#create subheader and columns
st.subheader("Main Metrics", divider='red')
#create a container to add a border
with st.container(border=True):
    col1, col2, col3 = st.columns(3) 
    # metrics showing: total Weekly_Sales, total Store, average Weekly_Sales
    #"${:,.0f}".format()
    col1.metric("Total Weekly Sales", "${:,.0f}".format(df_summed['Weekly_Sales'].values[0]))
    col2.metric("Total Number of Stores", df_summed["Store"])
    col3.metric("Average Weekly Sales", "${:,.0f}".format(df_summed['AvgWeekly_Sales'].values[0]))

st.header("")  #for spacing purposes  

#-----------Graphs-------------#
#create subheader and tabs
st.subheader("Graphs", divider='red')
tab1, tab2 = st.tabs(["Weekly Sales by Store", "Total Weekly Sales for a Specific Store"])

#sum sales by week and Store and build tab1 bar graphs
df_by_Store = selected_week_df.groupby("Store")["Weekly_Sales"]. sum().reset_index()
#st.dataframe(df_by_Store)
with tab1:
        fig = px.bar(df_by_Store, x = "Store" , y = "Weekly_Sales", title= "Weekly Sales by Store")
        st.plotly_chart(fig, use_container_width= True)

    
#average Weekly_Sales by Date and build tab2 bar graphs
df_by_Store = selected_week_df.groupby("Store")["Weekly_Sales"]. sum().reset_index()
#st.dataframe(df_by_Store)
with tab2:
        #grab unique Store
        Store = df["Store"].unique()
        #st.write(Store)
        #assign selected Store to a variable
        Store_selected = st.selectbox("Select Store", Store)
        #filter data based on selected Store
        selected_Store_df = df[df["Store"] == Store_selected]
        #st.dataframe(selected_week_df)
        df_by_Store = selected_Store_df.groupby("Store")["Weekly_Sales"]. sum().reset_index()
        #st.dataframe(df_by_Store)
        fig2 = px.bar(df_by_Store, x = "Store" , y = "Weekly_Sales", title= "Weekly Sales for Store")
        st.plotly_chart(fig2)