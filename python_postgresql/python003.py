from sqlalchemy import create_engine
import pandas as pd


## Create engine: engine
engine = create_engine('postgresql+psycopg2://mate:dataBASE**345**@localhost/ricardodellstore')

# Open engine in context manager
# Perform query and save results to DataFrame: df

with engine.connect() as con:
    rs = con.execute("SELECT * FROM categories")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

## Print the length of the DataFrame df 
print(len(df))

## Print the head of the DataFrame df 
print(df.head())


