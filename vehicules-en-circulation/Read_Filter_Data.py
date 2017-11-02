#vehicules-circulation-2016 dataset

#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df = pd.DataFrame()
#read_csv from pandas will read the csv file into dataframe(which is table like format)
df = pd.read_csv('vehicules-circulation-2016.csv')
#prints first 5 row of the dataframe
print(df.head(5))


#filters all records for columns NOSEQ_VEH and PHYS_SEX
print(df[["NOSEQ_VEH","PHYS_SEX"]])

#filters the records in which MARQ_VEH has value - HONDA
print(df[df["MARQ_VEH"] == "HONDA"])

#filters the records in which TYP_VEH_CATEG_USA has value - AU , or VT
print(df[(df["TYP_VEH_CATEG_USA"] == "AU") | (df["TYP_VEH_CATEG_USA"] == "VT")])

#filter by index (taking rows from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[20:30])

#filter by index (taking rows from 0 to 10, and columns 2 to 5)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[0:10,2:5])

#filter conditions and get particular column values for that condition.
print(df.loc[(df["COUL_ORIG"]=="BLA")&(df["NB_CYL"]== 4.0),"PHYS_SEX"])
