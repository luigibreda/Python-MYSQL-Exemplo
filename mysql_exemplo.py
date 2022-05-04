#!/usr/bin/env python
'''
MySQL CRUD (Criar, Ler, Modificar e Deletar) Operações utilizando Python e MySQL.
'''
__author__ = "Gabrielle Duarte Würzius"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "gablinda@gmail.com"
__status__ = "desenvolvimento"


# Import MySQLdb       $ sudo apt-get install python-mysqldb
import MySQLdb as mdb
import sys

# CREATE A NEW TABLE and INSERT SOME VALUES
def criarTabela(con):
    with con:

        cur = con.cursor()
        # Cria tabela e insere informações de teste
        cur.execute("DROP TABLE IF EXISTS TabelaTeste")
        cur.execute("CREATE TABLE TabelaTeste(Id INT PRIMARY KEY AUTO_INCREMENT, \
                     Name VARCHAR(25))")
        cur.execute("INSERT INTO TabelaTeste(Name) VALUES('Babbo Natale')")
        cur.execute("INSERT INTO TabelaTeste(Name) VALUES('Tizio')")
        cur.execute("INSERT INTO TabelaTeste(Name) VALUES('Caio')")
        cur.execute("INSERT INTO TabelaTeste(Name) VALUES('Sempronio')")
        cur.execute("INSERT INTO TabelaTeste(Name) VALUES('Giulio Cesare')")



# RETRIEVE TABLE ROWS
def lerTabela(con):
    with con:

        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM TabelaTeste")

        rows = cur.fetchall()

        for row in rows:
            print row["Id"], row["Name"]



# UPDATE ROW
def modificarTabela(con):
    with con:

        cur = con.cursor()

        cur.execute("UPDATE TabelaTeste SET Name = %s WHERE Id = %s",
            ("Nome Acaso", "4"))

        print "Número de linhas modificadas:",  cur.rowcount



# DELETE ROW
def deletarLinha(con):
    with con:

        cur = con.cursor()

        cur.execute("DELETE FROM TabelaTeste WHERE Id = %s", "2")

        print "Número de linhas deletas:", cur.rowcount



# CONFIGURA A CONEXÃO
try:
    con = mdb.connect('HOST_NAME', 'USER_NAME', 'PWD', 'DB_NAME');

    cur = con.cursor()
    # COMANDO PARA VERIFICAR VERSION
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()

    print "Banco de dados versão : %s " % ver


    # CRUD OPERAÇÕES
    criarTabela(con)
    lerTabela(con)
    modificarTabela(con)
    deletarLinha(con)



except mdb.Error, e:
    # TRATAMENTO DE EVEBNTUAIS ERROS
    print "Erro: %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)


finally:

    # SE A CONEXÃO AINDA ESTIVER ABERTA, FECHA ELA.
    if con:
        con.close()