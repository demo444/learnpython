# for this lesson, you will need to download the file at https://raw.githubusercontent.com/demo444/learnpython/master/sample.txt and put it in your python environment

# include the date/time manipulation package and pandas
import datetime
import pandas as pd

# Open the file and assign the file reader to the variable 'f'.  Read the contents of the file 'f' into the variable 'lines', split apart by line breaks.  This results in a list of lines stored in the variable 'lines'
with open('sample.txt','r') as f:
  lines = f.read().split("\n")

# Create an empty list to store the rows of data in variable 'rows'
rows = []

# For each line in the variable 'lines', split the words on each line into the variable 'words'.  Assign specific words on each line to the appropriate variables
for line in lines:
  words = line.split()
  if len(words) < 10:
    break
  date = words[1]
  time = words[3]
  pm = words[4][0:2]   # only take letters 0 through 1 from the AM/PM string, ignoring the comma that comes after
  amount = words[5].strip("$").replace(",", "") # remove '$' from beginning and any ',' from anywhere in the dollar amount
  paid = words[7]
  person = words[9].lower().strip('.')   # convert all names to lowercase, to ignore whether the names were capitalized, and remove trailing '.'
  
  # convert the date, time, and pm variables into a datetime number stored in the variable 'dt'
  dt = datetime.datetime.strptime("{} {} {}".format(date, time, pm), "%m/%d/%Y %I:%M %p")

  print("{},{},{},{},{}".format(dt.date(), dt.time(), amount, paid, person))

  # add this data row to the end of variable 'rows'
  rows.append({'date': dt.date(), 'time': dt.time(), 'amount': amount, 'paid': paid, 'person': person})

# see more commands you can use with strings at https://www.w3schools.com/python/python_ref_string.asp

# build a pandas DataFrame out of rows, and store it in variable 'df'
df = pd.DataFrame(rows)

# print the data frame
print(df)

# sort records by transaction date
print(df.sort_values(by='date'))

# sort records by transaction date, then time
print(df.sort_values(by=['date', 'time']))

# export cleaned data to a CSV file
df.to_csv('clean_data.csv')
