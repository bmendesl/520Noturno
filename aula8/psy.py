#!/usr/bin/python3

from psycopg2 import connect

try:
    con = connect(
        'host=localhost dbname=projeto user=admin password=4linux'
    )
    cur = con.cursor()

except Exception as e:
    print('ERRO: {}'.format(e))
    exit()


#cur.execute("select * from scripts;")
cur.execute("insert into scripts(nome,conteudo) values ('teste','algum conteudo por aqui');")
con.commit()

#print(cur.fetchall())

cur.close()
con.close()