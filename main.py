

#FUN FACT I DID EVERY THING WHICH WE LEARNED IN THAT CLASS!!!!I FEEL LIKE I FORGOT SOMETHING BUT I CAN NOT PUT MY FINGRE ON IT.


#importing pandas
import pandas as pd
#importing numpy
import numpy as np
#importing matplotlib
import matplotlib.pyplot as plt
#importing seaborn 
import seaborn as sb
#reading csv file
df=pd.read_csv("Penguins Data.csv")
print(df.head(11))
print(df.isnull().sum())
missing_values=["N/A","n/a","na","NA",np.nan]
df=pd.read_csv("Penguins Data.csv",na_values=missing_values)
print(df.isnull().sum())
# Visualize missing values using a heatmap (optimize by using a subset of data)
print(df.tail())
df1=sb.load_dataset("Penguins Data.csv")
sb.heatmap(df1.isnull(),yticklabels=False,annot=True)
plt.show()