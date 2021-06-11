#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Import data 
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
#%matplotlib inline

print("-----------Importing first dataset ------------")
df= pd.read_csv("./Texas_Hospital_capacity_over_time_by_TSA_region_new.csv")
df.info()


# In[16]:


df.head(20)




# handling missing value
#Remove Rows With Missing Values: where we see how to remove rows that contain missing values.
# drop rows with missing values
print("-----------Handling Missing Values---------------")
df.dropna(inplace=True)
df.info()



print("----------------Import second dataset--------------")
df1= pd.read_csv("./us-states.csv")
df1.tail(20)
df1.info()

df1.head()

df1_texas = df1[df1['state']=='Texas']

df1_texas


# # Data Merging


print("----------Merging the dataset ----------")
# joining the DataFrames 
display("The merged DataFrame") 
df_date_merge=pd.merge(df, df1_texas, on = "date", how = "inner") 
# data merge on basis of date

df_date_merge

df_date_merge.info()

#death vs cases
df_date_merge.plot.scatter(x='cases',y='deaths')
plt.show()
#cases vs available bed

df_date_merge.plot.scatter(x='Total Available Beds',y='Total Occupied Beds')
plt.show()



