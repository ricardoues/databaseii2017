from sqlalchemy import create_engine
import pandas as pd

## 
## http://stackoverflow.com/questions/9353822/connecting-postgresql-with-sqlalchemy

## Create engine: engine
engine = create_engine('postgresql+psycopg2://mate:password@localhost/ricardodellstore')

##  Open engine connection: con
con = engine.connect()

# Perform query: rs 
rs = con.execute("SELECT * FROM categories")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

print(df.head())
