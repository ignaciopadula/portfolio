import os

import cx_Oracle
import cx_Oracle as oracle
cx_Oracle.init_oracle_client(lib_dir="./helper/instantclient_18_5")

def visitOracle(sql, address):
    #conn = oracle.connect(user='usrnifi', password='usrnifi', dsn='10.250.11.15:1521/PTAXDESA')
    try:
        conn = oracle.connect(address)
        #conn = oracle.connect(user='usrnifi', password='usrnifi', dsn='10.250.11.15:1521/PTAXDESA')
        cursor = conn.cursor()
        cursor.execute(sql)
        # Leer el nombre de la columna del campo
        index = cursor.description
        row = 0
        for i in range(len(index)):
            row = index[i][0]
            break
        # Obtener información de devolución
        data = cursor.fetchone()
        result = data
        # Cerrar conexión, liberar recursos
        cursor.close()
        conn.close()
        return result
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 1017:
            print('Please check your credentials.')
            # sys.exit()?
        else:
            print('Database connection error: %s'.format(e))
        return None
