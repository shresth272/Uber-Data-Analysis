import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


df=pd.read_csv("UberDataset.csv")

print(df.head())    # Checking for data
print(df.tail())
print(df.info())    # Checking for Datatypes and not-null values 
print(df.isnull().sum())     # Count of not-null values



'''Data cleaning
1.Dealing with missig values.
2.Convert data into correct formate '''



df["PURPOSE"]=df["PURPOSE"].fillna("NOT SPECIFIED")    # Fill NAN values in PURPOSE with NOT SPECIFIED.




df["START_DATE"]=pd.to_datetime(df["START_DATE"],errors="coerce")    # Change START_DATE Datatype object to Datetime
df["END_DATE"]=pd.to_datetime(df["END_DATE"],errors="coerce")        # Change END_DATE Datatype object to Datetime


print(df.info())  
df.dropna(inplace=True)


df["DATE"]=pd.DatetimeIndex(df["START_DATE"]).date 
df["Time"]=pd.DatetimeIndex(df["START_DATE"]).hour
df["SHIFT"]=pd.cut(x=df["Time"],bins=[0,10,15,19,24],labels=["Morning","Afternoon","Evening","Night"])


print(df.head())


 # Ques1-In which category people book most uber ride ?

sns.countplot(df["CATEGORY"],color="c")
plt.show()

# Ques2-For which purpose do people book uber ride the most ?

sns.countplot(df["PURPOSE"],color="r")
plt.show()

# Ques3-At what time do people book cap the most from uber ?

sns.countplot(df["SHIFT"],color="y")
plt.show()



# Ques4-On which days of week do people book uber rides the most ?

df["DAY"]=df.START_DATE.dt.weekday
day_label={
    0:"mon",1:"tues",2:"wed",3:"thurs",4:"fri",5:"sat",6:"sun"
}

df["DAY"]=df["DAY"].map(day_label)

day_label=df.DAY.value_counts()
sns.barplot(x=day_label.index,y=day_label)
plt.xlabel("DAY")
plt.ylabel("COUNT")
plt.show()



df.to_csv("UberDataset.csv",index=False)