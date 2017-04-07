from sqlalchemy import create_engine
import pandas as pd


## Querying relational databases directly with pandas 
 
engine = create_engine('postgresql+psycopg2://mate:password@localhost/ricardodellstore')

## Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM categories", engine)

## Print head of DataFrame
print(df.head())



