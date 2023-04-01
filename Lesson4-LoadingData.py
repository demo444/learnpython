import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"

# read the specified url as a csv file, and create a pandas DataFrame variable 'cov' that contains the resulting data
cov = pd.read_csv(url, sep=',')

# print the first 3 rows
print(cov.head(3))

# print a line between output for readability
print('-----')

# convert date column from strings to actual date data types
cov["date"] = pd.to_datetime(cov["date"])

# delete unnecessary column
cov.drop(columns="fips", inplace=True)

# print some statistics about the data read into 'cov'
print(cov.info())
print(cov.describe())

# to get statistics on the columns of type 'object', we need to explicitly include that type, otherwise describe will only provide statistics on the numerical columns by default
print(cov.describe(include=np.object))

# print all the unique values for the 'state' column
print(np.sort(cov["state"].unique()))

# create a new variable dalCases that contains only the data for Dallas County
dalCases = cov[(cov["county"] == "Dallas") & (cov["state"] == "Texas")]
print(dalCases)

# plot the cases and deaths in the county by date
dalCases.plot(x='date', y=['cases','deaths'])
plt.xlabel('Date')
plt.ylabel('Number of People')

# save the plot to a file
plt.savefig('graph.png')
