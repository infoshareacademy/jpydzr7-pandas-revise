from sqlalchemy import create_engine
import pandas as pd

db_user = '<twoj-uzytkownik>'
db_password = '<twoje-haslo>'
db_host = 'localhost'
db_port = '3306'
db_name = 'django_rest_tutorial_infoshare'

engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

df = pd.read_sql('SELECT * FROM password_manager_passworddata', con=engine)
print(df.head())

df.to_excel('password_data_export.xlsx', index=False)


excel_df = pd.read_excel('password_data_export.xlsx')
print(excel_df.head())

excel_df.to_sql('password_data_export.sql', con=engine, if_exists='replace')