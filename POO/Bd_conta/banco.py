import sqlite3 as sq


def conectar():
    conn = sq.connect('banco.db')
    cursor = conn.cursor()
    return conn, cursor


def criar_tabela_cliente():
    conn, cursor = conectar()
    cursor.execute("""
    CREATE TABLE if EXISTS cliente(
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nasc TEXT NOT NULL
    )    
    """)
    conn.commit()
    cursor.close()
    conn.close()


def add_cliente(nome, data):
    conn, cursor = conectar()
    try:
        cursor.execute("""
        INSERT INTO cliente(nome, data_nasc)
        values (?, ?)
        """, (nome, data))
        conn.commit()
    except Exception as e:
        print(f'Erro {e}')
    finally:
        cursor.close()
        conn.close()


add_cliente('Pedrinho', '20/03/2000')
add_cliente('Carlito', '02/12/1999')

def listar_cliente():
    conn, cursor = conectar()
    cursor.execute("""
    SELECT * FROM cliente:
    """)
    listar_cliente = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return listar_cliente


for linha in listar_cliente():
    print(linha)
