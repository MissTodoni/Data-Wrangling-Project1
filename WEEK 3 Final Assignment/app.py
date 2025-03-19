#----------Import Packages----------#
import pandas as pd 
import streamlit as st 
import plotly.express as px



#----------Import Data----------#
#import data
df = pd.read_csv('restaurant_sales.csv')


#----------Initial Data Wrangling----------#
#transform order date to a datetime
df["order_date"] = pd.to_datetime(df["order_date"])

#date truncing to the month for comparisons and create as new column
df["order_month"] = df["order_date"].dt.to_period('M').dt.to_timestamp().dt.date



#----------Create Streamlit App----------#

#create a title
st.title('Restaurant Sales Dashboard')

#-----Data Selector-----#
#grab unique months

#assign selected month to a variable


#-----Data Filtering-----#
#filter data based on selected month

#create dataframe with summed sales and count of orders

# st.dataframe(df_selected_month_grouped)



#-----Metrics-----#
#create subheader and columns

# metrics showing: total sales, total orders, average order value




#-----Metrics-----#
#create subheader and tabs

#sum sales by month and category and build tab1 bar graphs

    
#sum sales by month and item_name and build tab2 bar graphs
