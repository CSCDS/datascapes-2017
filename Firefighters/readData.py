#Firefighters interventions dataset
#import pandas for reading csv file into dataframe
import pandas as pd

#read_csv from pandas will read the csv file into dataframe(which is table like format)
df = pd.read_csv('trips.csv')
#prints first 5 row of the dataframe
print(df.head(5))
