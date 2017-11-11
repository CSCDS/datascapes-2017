# Crime data 
# Link to dataset - http://donnees.ville.montreal.qc.ca/dataset/5829b5b0-ea6f-476f-be94-bc2b8797769a/resource/c6f482bf-bf0f-4960-8b2f-9982c211addd/download/interventionscitoyendo.csv
#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df = pd.DataFrame()

################## Reading data ###########################################################
#read_csv from pandas will read the csv file into dataframe(which is table like format)
df = pd.read_csv('interventionscitoyendo.csv')
#prints first 5 row of the dataframe
print(df.head(5))

#number of records in dataset
print("Number of records: "+str(len(df)))

############### Filtering data ############################
print("###################### Filtering columns ###############################################################")
#filters all records for columns CATEGORIE, DATE  and PDQ
print(df[["CATEGORIE","DATE","PDQ"]])

print("####################### Filtering on values of column ##################################################")
#filters the records in which CATEGORIE has value equal to Introduction
print(df[df["CATEGORIE"] == "Introduction"])

print("######################## Filtering on multiple values on column #########################################")
#filters the records in which PDQ is greater than 40 or QUART has value equal to nuit
print(df[(df["PDQ"] >40) | (df["QUART"] == "nuit")])

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
#Gives value of DATE column where CATEGORIE is "Introduction" and QUART is "soir"
print(df.loc[(df["CATEGORIE"] == "Introduction") & (df["QUART"]=="soir"),"DATE"])
