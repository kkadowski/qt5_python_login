# qt5_python_login

QT5 + Python + Postgresql based login app.

Requirements:
- PostgreSQL 12.9
- Python 3
- QT5

Before you start to explore project create database using:

        CREATE DATABASE customers;

and users table on Postgresql server using:

    python sql.py


FILES:

- database.ini - configuration of connection
- pycompat.py - compatibility check 
- db_con.py - file with class dbConnection
- sql.py - creation of databas, table and first user
- login.py - login app
