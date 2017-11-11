# 1.Firefighters interventions - 2015 dataset
#Dataset link - http://donnees.ville.montreal.qc.ca/dataset/701683f0-a838-4fe0-b4d6-a4964d9ea7f0/resource/9e67d2f3-9104-4af4-aac4-022df621a749/download/donneesouvertes-interventions-sim.csv

#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df1 = pd.DataFrame()

################## Reading data ###########################################################
#read_csv from pandas will read the csv file into dataframe(which is table like format)
print("Dataset 1: Interventions du SIM - 2015 à aujourd'hui")
df1 = pd.read_csv('donneesouvertes-interventions-sim.csv')
#prints first 5 row of the dataframe
print(df1.head(5))

#number of records in dataset
print("Number of records: "+str(len(df1)))

############### Filtering data ############################
print("###################### Filtering columns ###############################################################")
#filters all records for columns incident_nbr, latitude  and longitude
print(df1[["incident_nbr","latitude","longitude"]])

print("####################### Filtering on values of column ##################################################")
#filters the records in which nom_ville has value Montreal
print(df1[df1["nom_ville"] == "Montreal"])

print("######################## Filtering on multiple values on column #########################################")
#filters the records in which latitude is greater than 45.15 or longitude has value less than -73.67
print(df1[(df1["latitude"] >45.15) | (df1["longitude"] <-73.67 )])

print("######################### Slice on rows (by index) #######################################################")
#filter by index (taking rows from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(df1.iloc[20:30])

print("########################## Slice on columns(by index)######################################################")
#filter by index (taking columns from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(df1.iloc[:,2:7])

print("########################## Slice on row and column(by index) ############################################")
#filter by index (taking rows from 0 to 10, and columns 2 to 5)
# Remember that Python does not slice inclusive of the ending index.
print(df1.iloc[0:10,2:5])

print("########################## Multiple filters on column and get value of other column #######################")
#filter conditions and get particular column values for that condition.
print(df1.loc[(df1["nom_ville"]=="Montreal") & (df1["nom_arrond"]=="Plateau Mont-Royal"),"nombre_unites"])


# 2.Firefighters interventions 2005 -2015 dataset
#Dataset link - http://donnees.ville.montreal.qc.ca/dataset/701683f0-a838-4fe0-b4d6-a4964d9ea7f0/resource/3456b299-5dee-470f-9b9a-8839e9d160e4/download/donneesouvertes-interventions-sim-2005-2014.csv

#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df2 = pd.DataFrame()

################## Reading data ###########################################################
#read_csv from pandas will read the csv file into dataframe(which is table like format)
print("Dataset 2 - Interventions du SIM - 2005-2014 Populaire")
df2 = pd.read_csv('donneesouvertes-interventions-sim.csv')
#prints first 5 row of the dataframe
print(df2.head(5))

#number of records in dataset
print("Number of records: "+str(len(df2)))

frame1 =df1[df1["nom_arrond"] == "Lachine"]
frame2 = df2[df2["nom_arrond"] == "Lachine"]

#Concatenate the frames having nom_arrond = "Lachine" in both dataset.
concat_df = pd.concat([frame1,frame2])
print(concat_df)


# 3.Tableau concordance : Type incident - Description
#Dataset link - http://donnees.ville.montreal.qc.ca/dataset/701683f0-a838-4fe0-b4d6-a4964d9ea7f0/resource/77827f34-bce7-4484-83c7-24873bd59f75/download/type-interventions-descriptions20161122.csv
#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df3 = pd.DataFrame()



################## Reading data ###########################################################
#read_csv from pandas will read the csv file into dataframe(which is table like format)
print("Dataset 3: Tableau concordance : Type incident - Description")
df3 = pd.read_csv('type-interventions-descriptions20161122.csv')
#prints first 5 row of the dataframe
print(df3.head(5))

#number of records in dataset
print("Number of records: "+str(len(df3)))
