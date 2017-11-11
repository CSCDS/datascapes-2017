# 1. Travel time on road segment (using bluetooth detection)
# Dataset link - http://depot.ville.montreal.qc.ca/temps_parcours_bluetooth/trips.csv
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


# 2. Road segments for collecting travel time
# Dataset link - http://donnees.ville.montreal.qc.ca/dataset/a8f68bfa-5ead-4dda-ab52-b48e45ce9ea0/resource/5c342221-14c1-4593-9e2e-d1044b41dd90/download/bornes.csv

#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
dp = pd.DataFrame()

################## Reading data ###########################################################
#read_csv from pandas will read the csv file into dataframe(which is table like format)
dp = pd.read_csv('bornes.csv')
#prints first 5 row of the dataframe
print(dp.head(5))

#number of records in dataset
print("Number of records: "+str(len(dp)))

############### Filtering data ############################
print("###################### Filtering columns ###############################################################")
#filters all records for columns SrcDetectorId, channel_name  and last_poll_time
print(dp[["SrcDetectorId","channel_name","last_poll_time"]])

print("####################### Filtering on values of column ##################################################")
#filters the records in which LineDistance_m has value greater than 2000
print(dp[dp["LineDistance_m"] > 2000])

print("######################## Filtering on multiple values on column #########################################")
#filters the records in which SrcChannelId is less than 20 or DestChannelId has value less than 20
print(dp[(dp["SrcChannelId"] <20) | (dp["DestChannelId"] < 20)])

print("######################### Slice on rows (by index) #######################################################")
#filter by index (taking rows from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(dp.iloc[20:30])

print("########################## Slice on columns(by index)######################################################")
#filter by index (taking columns from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(dp.iloc[:,2:7])

print("########################## Slice on row and column(by index) ############################################")
#filter by index (taking rows from 0 to 10, and columns 2 to 5)
# Remember that Python does not slice inclusive of the ending index.
print(dp.iloc[0:10,2:5])

print("########################## Multiple filters on column and get value of other column #######################")
#Gives value of LinkName column where RouteDirectionName is N and active is 1.
print(dp.loc[(dp["RouteDirectionName"]=="N") & (dp["active"]==1),"LinkName"])


print("############################ Merging(Inner join) the datasets #########################################################")
#Performing outer join on both the above datasets on SrcDetectorId and DestDetectorId
merged_df1 = pd.DataFrame()
merged_df1 = pd.merge(df, dp,how='inner', on=['SrcDetectorId', 'DestDetectorId'])
print(merged_df1.head())

print("############################ Merging(Outer join) the datasets #########################################################")
#Performing inner join on both the above datasets on SrcDetectorId and DestDetectorId
#Other possible merge operations are left join, right join (Specify how ='left' and how ='right' respectively)
merged_df2 = pd.DataFrame()
merged_df2 = pd.merge(df, dp,how='outer', on=['SrcDetectorId', 'DestDetectorId'])
print(merged_df2.head())
