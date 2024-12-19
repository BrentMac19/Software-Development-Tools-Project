
import pandas as pd
import streamlit as st
import plotly.express as px

#importing dataframe
df = pd.read_csv("vehicles_us.csv")

#-------------------------------------#
#Head of Page
st.header("US Car Market Data")
st.markdown("""
    This app recieved the data set on car sales advertisements 
""")

#--------------------------------------#
#sidebar
st.sidebar.header('User Input Features for Histogram chart')
st.sidebar.markdown("""
This feature will update the histogram to display the distribution of the model_year without outliers Skewing the data
""")

checked=st.sidebar.checkbox("remove outliers")
    
#--------------------------------------#
#About
expand_bar=st.expander("About")
expand_bar.markdown("""
* **Python libraries:** pandas, plotly.express, streamlit
                    
This project is going to provide visual data using plotly.express to show the
correlation between odometer and prices in car sales, 
and the distribution between model years.                   
                    """)
#----------------------------#

#displaying dataframe
st.dataframe(df)

st.markdown("""
    \n\n
    *Scatter Plot* will show the negative correlation between, the price of a vehicle and odometer
    The figure is color cordinated by condition of the car
            """)
#filtering outliers for scatterplot data points
filtered_price_odometer_df=df.query("price<=100000 & odometer<=500000")
#Displaying figure Scatter plot
price_odometer_fig=px.scatter(filtered_price_odometer_df, y='price', x='odometer',color='condition',
           height=500,template="simple_white",
           title='Correlation Between Price vs. Odometer',
           labels= dict(
               price='Price in USD',
               odometer='Odometer in mi',
               condition="Condition"
           ))
price_odometer_fig.update_layout(font_family="Rockwell",
                                legend=dict(orientation='h',title='',y=1.1,x=1,
                                              xanchor='right',yanchor='top')
                                 ) 
price_odometer_fig.update_yaxes(tickprefix="$")
                                
st.plotly_chart(price_odometer_fig, use_container_width=True)

st.markdown("""
    \n\n
    *Histogram* will show the distribution between, the model year of the vehicle. the 
            graph is going to be catergorized by vehicle type.
            """)
#removing NULL values
model_df_filtered=df.dropna(subset='model_year')
#checkbox condition
if checked:
    model_df_filtered=model_df_filtered.query("model_year >= 1990")
    


#model_year figure
model_fig = px.histogram(model_df_filtered,x='model_year',color='type',
                         height=600, template="simple_white",
                         title="Distribution for Vehicle Model Year",
                         labels= dict(
                            model_year='Model Year',
                            count='Count',
                            type="Vehicle Type"
                            ))
model_fig.update_layout(font_family="Rockwell",
                                legend=dict(orientation='h',title='',y=1.1,x=1,
                                              xanchor='right',yanchor='top'))

st.plotly_chart(model_fig, use_container_width=True)






