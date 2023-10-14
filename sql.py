"""
Creating table: users
Inserting user: admin, email: admin@example.com, password: admiadmin in MD5
"""
import os
from db_con import dbConnection


db = dbConnection()
db.connect()

db.execute("create table if not exists users(id_user SERIAL primary key, f_name VARCHAR(16) not null, l_name VARCHAR(32) not null, email VARCHAR (128) not null, pass VARCHAR(64), privil VARCHAR(1) default '1', created timestamp)")
db.commit()

db.execute("insert into users (f_name, l_name, email, pass, created) values ('admin', 'admin', 'admin@example.com', 'f6fdffe48c908deb0f4c3bd36c032e72', now())")
db.commit()
db.close()




