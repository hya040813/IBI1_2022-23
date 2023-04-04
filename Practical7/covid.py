#Importing a dataset
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#change the working directory to where my full_data.csv file is stored
os.chdir('C:/Users/Administrator/IBI1_2022-23/IBI1_2022-23/Practical7/')
# use the pandas library to read the content of the .csv file into a dataframe >
covid_data = pd.read_csv('full_data.csv')
covid_data.head()
covid_data.info()
covid_data.describe()
covid_data.iloc[0:1000:100,1]
covid_data,loc[0:81,'total_cases']
#Filter out rows with a location value of Afghanistan
Afghanistan = []
location = covid_data.loc[:,"location"]
for i in location:
    if i=="Afghanistan":
        Afghanistan.append(True)
    else:
        Afghanistan.append(False)
covid_data.loc[Afghanistan,"total_cases"]
#Filter out rows with a country value of World
country = []
for i in location:
    if i=="World":
        country.append(False)
    else:
        country.append(True)
world = [not i for i in country]
country_data = covid_data.loc[country,:]
world_data = covid_data.loc[world,:]
#Filter out rows with a dates value of 2020-03-31
March_31_2020 = []
date = country_data.loc[:,"date"]
for i in date:
    if i=="2020-03-31":
        March_31_2020.append(True)
    else:
        March_31_2020.append(False)
#create new_data frame
new_data = country_data.loc[March_31_2020,1:4]
#calculate means of specific datas
mean_new_cases = np.mean(new_data.iloc[0:195,1])
print(mean_new_cases)
mean_new_deaths = np.mean(new_data.iloc[0:195,2])
print(mean_new_deaths)
#use matplotlib.pyplot to plot the data
plt.boxplot(new_data.loc[:,"new_cases"])
plt.title("new_cases of different countries on 31 March 2020")
plt.show()
plt.boxplot(new_data.loc[:,"new_deaths"])
plt.title("new_deaths of different countries on 31 March 2020")
plt.show()