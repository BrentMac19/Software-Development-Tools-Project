# Software-Development-Tools-Project
#----------------------------------------#
#Welcome to my Application!
The purpose of this application was to read data provided in a CSV file that has information of US car Advertisments,
the goal of this project was to read, and explore the data and find some small findings with the data.
#------------------------------------------------------------------------------------------------------------------------#
#INFO 
What you will find in this repositiory is the enviroment necessary to run the application, the Jupiter Notebook that was used to explore the data before translating it to the application, the vechiles_us.csv file which is used to read the data to our notebook and application, and the README file which has all the information you need to see what the intentions for the app will be, and necessary packages that will be needed
#------------------------------------------------------------------------------------------------------------------------#
#NEEDED PACKAGES
enviornment was created using .venv, the necessary packages for this project will be:

PANDAS 
PLOTLY.EXPRESS
STREAMLIT
IPYKERNEL
NBFORMAT
#------------------------------------------------------------------------------------------------------------------------#
It is  best to update these packages if you have not done so in a while.
#------------------------------------------------------------------------------------------------------------------------#
#NOTEBOOK
In the notebook you will find some basic EDA (Exploration Data Analysis) using jupiter notebook, this is were we read the csv file and familiarized ourselves with the data presented to us, we then proceeded to explore the answers we were looking to solve

WHAT WERE WE LOOKING TO ANSWER:
Is there a correlation between the Vehicle ODOMETER reading and the Vechiles asking price?
What is the distribution between the Vehicles MODEL_YEAR?
#------------------------------------------------------------------------------------------------------------------------#
#APP.PY
<------Header------->
When the application is launched you should see a title called "US Car Market Data"
followed by a description of where the data was retrieved
below will be an About drop list that you can click and it will share some information about the application
<-----Body----------->
The body begins with displaying the dataset for the user to see to familiarize themselves with the data that was provided, we can see what information is being compared at hand before graphs are displayed
#scatterplot
After that we get a brief description of the scatterplots correlation and the results of the graph explaining the correlation between the PRICE AND ODOMETER, The graph will have a Title called "Correlation between Price vs. Odometer"
the graph has a legend which shows it is color cordinated by Condition of the car, this legend is interactive and if clicked upon will remove selected conditon from the graph, if clicked again that data will reload to the plot.
#histogram
After the scatter plot we will see another brief description of the histogram and its results. The histogram is looking for the disribution of the MODEL_YEAR and is color cordinated by vehicle TYPE which is also a fully interactive legend that will update the histogram as you filter TYPE.
#sidebar
The histogram model can also be changed using the side bar funtion to remove outliers of the function, you can see the data is drastically skewed to the right, and it is hard to visualize the data with the effect of the outliers. so we can filter them out using the check box funtionaility. click the arrow opening the side bar and you will see a descprition of the outlier checkbox removale, if you cick the check box it will filter all the data for the model year from 1990 and greater (to 2019).




