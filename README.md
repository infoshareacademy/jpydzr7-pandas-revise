# Pandas Revise

## Instalacja

* krokiem pierwszym jest zainstalowanie wszystkich bibliotek do obsługi bazy danych i samej biblioteki Pandas, w tym celu zainstaluj biblioteki znajdujące się w pliku `requirements.txt`. Do tego można użyć komendy 
```terminaloutput
pip install -r requirements.txt
```

W skład pliku `requirements.txt` wchodzą: pandas, sqlalchemy, pymysql, cryptography, openpyxl.

## Wczytanie danych z plików/bazy danych do Pandas

Wczytywanie danych z pliku i z bazy danych w Pandas odbywa się na podobnej zasadzie. Pandas posiada wbudowane funkcję do wczytywania zbiorów danych.

### CSV
W przypadku plików `csv` wczytywanie danych odbywa się poprzez wykonanie funkcji, jako argument podajemy ścieżkę do naszego pliku csv. Funkcja `head()` wykonana na zbiorze danych pozwala na sprawdzenie czy został wczytany poprawny zbiór. Wyświetla ona kilka pierwszych kolumn i wierszy w zbiorze.
```python
import pandas as pd

df = pd.read_csv('password_manager_passworddata.csv')
print(df.head())
```

Wyjście funkcji `head()`

```
   id                  created_at  ... username  user_id
0   1  2025-04-27 08:08:04.878926  ...   User_1        1
1   2  2025-04-27 08:08:24.422871  ...   user_1        1
2   3  2025-04-27 08:08:41.326024  ...   user_1        1
3   4  2025-04-27 08:09:13.270054  ...   user_1        1
4   5  2025-04-27 08:09:32.627152  ...     Test        1
```

### Excel

Pandas czyta excela podobnie jak plik csv, jedyną różnicą jest użycie innej funkcji, `read_excel` przyjmuje jako parametr ścieżkę do pliku excelowego.
```python
import pandas as pd

df = pd.read_excel('password_manager_passworddata.xlsx')
print(df.head())
```

### MySQL
W przypadku mysql sytuacja jest bardzo podobna od strony biblioteki pandas, z tą różnicą, że wywołujemy funkcję `read_sql` która przyjmuje 2 parametry, pierwszy to kwerenda sql którą chcemy wykonać na bazie danych, drugie to `connection`, czyli połączenie z bazą danych na której kwerenda ma być wykonana. Można do tego wykorzystać wiele bibliotek do łączenia się z bazą danych, my wykorzystamy pymsql, sqlalchemy. `create_engine` tworzy połączenie z bazą danych, jako dwie pierwsze wartości podajemy bazę danych `mysql` i bibliotekę jakiej w pythonie użyjemy do połączenia się z mysql (czyli `pymysql`), następnie tworzymy nasz 'connection string', podajemy kolejno dane `użytkownik:hasło@host:port/baza danych`
```python
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
```

## Manipulowanie danymi w pandas

Pandas poza wczytywaniem danych i zapisem ich może też tworzyć nowe ramki danych oraz wybierać dane z innych, podstawowymi akcjami jakie można zrobić z ramką danych jest wybór kolumny, wybranie unikalnych elementów z kolumny, sprawdzenie ile razy w kolumnie występuję dana wartość lub grupowanie po kolumnie
```python
import pandas as pd
df = pd.read_excel('password_manager_passworddata.xlsx')

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
```

## Zapis zbioru danych

### CSV
Zapisywanie do CSV jest podobne do czytania z pliku csv, wystarczy wykonać na ramce danych funkcję `to_csv` która jako argument przyjmuje nazwę pliku.
```python
df.to_csv('password_data_export.xlsx')
```
### Excel
W excelu zasada jest podobna jak w CSV, z tą różnicą, że wykonujemy funkcję `to_excel`
```python
df.to_excel('password_data_export.xlsx', index=False)
```
### MySQL
W przypadku mysql jedyne o czym musimy pamiętać to, że na ramce danych wykonujemy funkcję `to_sql` podajemy `connection` ten sam który wykorzystaliśmy do `read_sql` i w tym wypadku podajemy nazwę tabeli jaka ma się utworzyć w bazie danych, zamiast nazwy pliku.
```python
df.to_sql('password_data_export', con=engine, if_exists='replace')
```
