from sqlalchemy import create_engine

## 
## http://stackoverflow.com/questions/9353822/connecting-postgresql-with-sqlalchemy

## Create engine: engine
engine = create_engine('postgresql+psycopg2://mate:password@localhost/ricardodellstore')

## Save the table names to a list: table_names 
table_names = engine.table_names()

## Print the table names 
print(table_names)
