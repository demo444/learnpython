# we must first include the numpy and pandas python packages, for manipulating arrays and DataFrames
import numpy as np
import pandas as pd

# create a list of 7 amounts and assign it to variable 'l'
l = [240,530,350,230,420,240,1200]

# print the whole list
print(l)

# print the first item (python always counts from 0, not 1!)
print(l[0])

# print the 6th item (remember the 7 items in the list are numbered 0 through 6, so item 6 is the last item)
print(l[6])

# print the number of items
print("There are {} items".format(len(l)))

# print each item in the list 'l', one line at a time
print("----")
for amount in l:
  print(amount)

# print items starting at 1 and stopping before 3 (so, item 1 & 2) in the list 'l', one line at a time
print("----")
for i in range(1,3):
  print(l[i])

# print just the part of the list including item 1 & 2
print(l[1:3])

# print a string
s = "The brown fox."
print(s)
print("The string is: {}".format(s))

# print the first item and the middle letters 4 through 8 of the string (remember, always count from 0!)
print("The string starts with '{}' and the middle is '{}'".format(s[0], s[4:9]))

# turn our list into numpy array
a = np.array(l)
print(a)

# print the sum of the new array
print("The sum is {}".format(np.sum(a)))

# sort the array, store it in the variable 'sorta', and print the sorted array
sorta = np.sort(a)
print(sorta)

# make a pandas DataFrame from the numpy array 'a'
df = pd.DataFrame(a)
print(df)

# make a pandas DataFrame from the original list 'l'
df = pd.DataFrame(l)
print(df)

# make a 2-D pandas DataFrame from multiple lists
listOfNames = ['alice', 'bob', 'jim', 'mark', 'alice', 'mark', 'alice']
df = pd.DataFrame([l, listOfNames], index=['Amount', 'Person'])
print(df)

# transpose rows and columns
df = df.T
print(df)

# print summary of DataFrame
print(df.describe())

# print row 2, column 1 (counting from 0!)
print("Row 2, Column 1 is: {}\n".format(df.iloc[2, 1]))

# print DataFrame sorted by amount, from highest to lowest
print(df.sort_values(by='Amount', ascending=False))

# print just the column of people from the DataFrame
print("---------\nJust person column:")
print(df['Person'])

# print the number of transactions of each person
print(df['Person'].value_counts())

# print rows 0 through 3 of the DataFrame
print(df[0:4])

# print only the rows that include alice
print(df[df['Person'] == 'alice'])

# print the average of only Alice's transactions
print(df[df['Person'] == 'alice'].mean())

# print only the rows that include transactions above 400
print(df[df['Amount'] > 400])

# export just Alice's transactions to a csv file
# this may not work properly in a web-based python client
df[df['Person'] == 'alice'].to_csv('alice.csv')

