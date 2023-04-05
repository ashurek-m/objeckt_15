import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = r'ZYFRA\SQLEXPRESS'
DATABASE_NAME = 'Industry'

connection = f'''
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    uid=directus;
    pwd=12345;
    '''

conn = odbc.connect(connection)
print(conn)
