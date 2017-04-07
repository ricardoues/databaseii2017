from sqlalchemy import create_engine
import pandas as pd


## Querying relational databases directly with pandas 
 
engine = create_engine('postgresql+psycopg2://mate:password@localhost/ricardodellstore')

## Execute query and store records in DataFrame: df
## INNER JOIN CLAUSE IS USED
## We obtain movies and its names.
df = pd.read_sql_query("SELECT A.categoryname, B.title FROM categories A INNER JOIN products B ON A.category = B.category", engine)

## Print head of DataFrame
print(df.head())



