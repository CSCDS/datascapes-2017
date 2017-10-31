
#import pandas for reading csv file into dataframe
import pandas as pd

#intialize dataframe
df = pd.DataFrame()
#read_csv from pandas will read the csv file into dataframe(which is table like format)
df = pd.read_csv('donneesouvertes-interventions-sim.csv')
#prints first 5 row of the dataframe
print(df.head(5))


#filters all records for columns incident_nbr, latitude  and longitude
print(df[["incident_nbr","latitude","longitude"]])

#filters the records in which nom_ville has value Montreal
print(df[df["nom_ville"] == "Montreal"])

#filters the records in which latitude is greater than 45.15 or longitude has value less than -73.67
print(df[(df["latitude"] >45.15) | (df["longitude"] <-73.67 )])

#filter by index (taking rows from 20 to 30)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[20:30])

#filter by index (taking rows from 0 to 10, and columns 2 to 5)
# Remember that Python does not slice inclusive of the ending index.
print(df.iloc[0:10,2:5])

#filter conditions and get particular column values for that condition.
print(df.loc[(df["nom_ville"]=="Montreal") & (df["nom_arrond"]=="Plateau Mont-Royal"),"nombre_unites"])
