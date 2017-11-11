#vehicules-circulation-2016 dataset
#dataset link - https://saaq.gouv.qc.ca/donnees-ouvertes/vehicules-circulation/vehicules-circulation-2016.csv
#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df = pd.DataFrame()

################ Reading data #################################################################################
#read_csv from pandas will read the csv file into dataframe(which is table like format)
df = pd.read_csv('vehicules-circulation-2016.csv')
#prints first 5 row of the dataframe
print(df.head(5))

#number of records in dataset
print("Number of records: "+str(len(df)))

############### Filtering data ################################################################################
print("###################### Filtering columns ###############################################################")
#filters all records for columns NOSEQ_VEH and PHYS_SEX
print(df[["NOSEQ_VEH","PHYS_SEX"]])

print("####################### Filtering on values of column ##################################################")
#filters the records in which MARQ_VEH has value - HONDA
print(df[df["MARQ_VEH"] == "HONDA"])

print("######################## Filtering on multiple values on column #########################################")
#filters the records in which TYP_VEH_CATEG_USA has value - AU , or VT
print(df[(df["TYP_VEH_CATEG_USA"] == "AU") | (df["TYP_VEH_CATEG_USA"] == "VT")])


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
#Gives value of PHYS_SEX column where COUL_ORIG is BLA and NB_CYL is 4.0
print(df.loc[(df["COUL_ORIG"]=="BLA")&(df["NB_CYL"]== 4.0),"PHYS_SEX"])
