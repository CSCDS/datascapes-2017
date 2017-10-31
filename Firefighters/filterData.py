#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df = pd.DataFrame()
#read_csv from pandas will read the csv file into dataframe(which is table like format)
df = pd.read_csv('trips.csv')
#prints first 5 row of the dataframe
print(df.head(5))


#filters all records for columns SrcDetectorId, Speed_kmh  and TravelTime_s
print(df[["SrcDetectorId","Speed_kmh","TravelTime_s"]])

#filters the records in which Speed_kmh has value greater than 80
print(df[df["Speed_kmh"] > 80])

#filters the records in which Speed_kmh is less than 80 or TravelTime_s has value less than 100
print(df[(df["Speed_kmh"] <80) | (df["TravelTime_s"] < 100)])

#filter by index (taking rows from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[20:30])

#filter by index (taking rows from 0 to 10, and columns 2 to 5)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[0:10,2:5])

#filter conditions and get particular column values for that condition.
print(df.loc[(df["TravelTime_s"]>100) & (df["TravelTime_s"]<180),"TripStart_dt"])
