import pymysql

import db_config

connection = pymysql.connect(host='localhost',
                             user=db_config.db_user,
                             passwd=db_config.db_passwd)
try:
            with connection.cursor() as cursor:
                sql="CREATE DATABASE IF NOT EXISTS CRIMEMAP"
                cursor.execute(sql)
                sql="""CREATE TABLE IF NOT EXISTS CRIMEMAP.crimes(
id int NOT NULL AUTO_INCREMENT,
latitude FLOAT(10,6),
longitude FLOAT(10,6),
date DATETIME,
category VARCHAR(50),
description VARCHAR(1000),
updated_at TIMESTAMP,
PRIMARY KEY (ID)
)"""
                cursor.execute(sql);
                connection.commit()
finally:
                connection.close()