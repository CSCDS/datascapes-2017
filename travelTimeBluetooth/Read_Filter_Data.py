#Travel time on road segment (using bluetooth detection)
#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df = pd.DataFrame()

################## Reading data ###########################################################
#read_csv from pandas will read the csv file into dataframe(which is table like format)
df = pd.read_csv('trips.csv')
#prints first 5 row of the dataframe
print(df.head(5))

#number of records in dataset
print("Number of records: "+str(len(df)))

############### Filtering data ############################
print("###################### Filtering columns ###############################################################")
#filters all records for columns SrcDetectorId, Speed_kmh  and TravelTime_s
print(df[["SrcDetectorId","Speed_kmh","TravelTime_s"]])

print("####################### Filtering on values of column ##################################################")
#filters the records in which Speed_kmh has value greater than 80
print(df[df["Speed_kmh"] > 80])

print("######################## Filtering on multiple values on column #########################################")
#filters the records in which Speed_kmh is less than 80 or TravelTime_s has value less than 100
print(df[(df["Speed_kmh"] <80) | (df["TravelTime_s"] < 100)])

print("######################### Slice on rows (by index) #######################################################")
#filter by index (taking rows from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[20:30])

print("########################## Slice on columns(by index)######################################################")
#filter by index (taking columns from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[:,2:7])

print("########################## Slice on row and column(by index) ############################################")
#filter by index (taking rows from 0 to 10, and columns 2 to 5)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[0:10,2:5])

print("########################## Multiple filters on column and get value of other column #######################")
#filter conditions and get particular column values for that condition.
print(df.loc[(df["TravelTime_s"]>100) & (df["TravelTime_s"]<180),"TripStart_dt"])
