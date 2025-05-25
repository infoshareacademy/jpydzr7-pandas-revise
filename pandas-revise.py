from sqlalchemy import create_engine
import pandas as pd

#loading data

# db_user = '<twoj-uzytkownik>'
# db_password = '<twoje-haslo>'
db_user = 'django_user'
db_password = 'root'
db_host = 'localhost'
db_port = '3306'
db_name = 'django_rest_tutorial_infoshare'

df = pd.read_csv('password_manager_passworddata.csv')
print(df.head())

df = pd.read_excel('password_manager_passworddata.xlsx')
print(df.head())

engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

df = pd.read_sql('SELECT * FROM password_manager_passworddata', con=engine)
print(df.head())

# Manipulate data
user_id_passwords = df.groupby('user_id').size()
print("user passwords count", user_id_passwords)

service_name = df['service_name']
print(service_name)

unique_passwords = df['password'].unique()
print("unique passwords", unique_passwords)

data = df[['email', 'password']]

print("select email and password columns", data)

data_test_password = data[data['password'] == 'Test1234!']
print("Passwords that equals Test1234!",data_test_password)

# Save data

df.to_csv('password_data_export.xlsx')
df.to_excel('password_data_export.xlsx', index=False)

df.to_sql('password_data_export', con=engine, if_exists='replace')