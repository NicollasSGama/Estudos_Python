# -*- coding:utf-8 -*-

import sqlite3 as sq


def conector():
    conn = sq.connect('appfinanceiro.db')
    cursor = conn.cursor()

    return conn, cursor


def criarTabelaUsuario():
    conn, cursor = conector()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def addUsuario(nome, senha, telefone):
    conn, cursor = conector()
    cursor.execute("""
    INSERT INTO usuario (nome, senha, telefone)
    values (?, ?, ?)
    """, (nome, senha, telefone))
    # Máscara para garantir que não seja possível pôr um comando sql seja rodado na
    # entrada de string - uma seguraça
    conn.commit()
    cursor.close()
    conn.close()


criarTabelaUsuario()
addUsuario('MARIA', '1234', '(11)95041-1234')
