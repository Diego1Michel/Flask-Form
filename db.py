import pymysql
#conexão com o mySql
connection=pymysql.connect(host="localhost", user = "root", passwd="00000000", database="FLASK", port=3306)
cursor = connection.cursor()

# função add dados ao banco
def add_text(name, email, cidade, endereco, telefone, data_nascimento):
    cursor.execute("INSERT INTO form(ID, nome, email, cidade, endereco, telefone,data_nascimento) VALUES (DEFAULT, %s,%s,%s,%s,%s,%s)", (name, email, cidade, endereco, telefone, data_nascimento))
    connection.commit()
    return 1

# função apresenta dados guardados
def get_data():
    cursor.execute("SELECT * FROM form")
    rows = cursor.fetchall()
    return rows
