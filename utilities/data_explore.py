import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect('../data/db/history')
df = pd.read_sql_query('SELECT * from me', con)

df['date'] = pd.to_datetime(df['date'])

df['temperature'] = pd.to_numeric(df['temperature'])

df.head()

df.plot(x='date', y='temperature')

plt.show()