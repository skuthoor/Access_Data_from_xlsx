import sqlite3
import pandas as pd
  
conn = sqlite3.connect('blood_bank.db')
  
# Load CSV data into Pandas DataFrame
stud_data = pd.read_csv('blood_bank.csv')
# Write the data to a sqlite table
stud_data.to_sql('blood_bank', conn, if_exists='replace', index=False)
  
# Create a cursor object
cur = conn.cursor()

# Close connection to SQLite database
conn.close()