print("script started")
from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine('sqlite:///beauty_trends.db')

with engine.connect() as conn:
    df = pd.read_sql(text(open('queries.sql').read()), conn)
    print(df.to_string())
