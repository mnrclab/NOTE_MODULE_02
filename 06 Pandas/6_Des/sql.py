import pandas as pd 
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+mysqlconnector://root:kahfi2008@localhost/world?host=localhost?port=3306")

conn = engine.connect()
results = conn.execute("SELECT * from city").fetchall()
df1 = pd.DataFrame(results)
df1.columns = results[0].keys()
print(df1.head(3))
