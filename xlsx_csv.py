import pandas as pd

read_file = pd.read_excel (r'/home/skuthoor/Desktop/flask/python/Access_Data_from_xlsx/List_of_Blood_Centers_in_Kerala.xlsx')
read_file.to_csv (r'/home/skuthoor/Desktop/flask/python/Access_Data_from_xlsx/blood_bank.csv', index = None, header=True)

print('converted')