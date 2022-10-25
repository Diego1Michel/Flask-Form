import pymysql
import smtplib, ssl

#conexão com o mySql
connection=pymysql.connect(host="localhost", user = "root", passwd="00000000", database="testes", port=3306)
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

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 587)
email = 'topcars.t22@gmail.com'
senha = 'top2022cars'

# Abre o banco de dados
db = pymysql.connect(host="localhost", user = "root", passwd="00000000", database="testes", port=3306)

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = " SELECT ID, nome, email, cidade, endereco, telefone,data_nascimento FROM form"
# executa o SQL
cursor.execute(sql)

# lista a base.
results = cursor.fetchall()

#loga no SMTP
smtp.login(email,senha)

for row in results:
    id = row[0]
    email_destino = row[2]
    titulo = "Bem Vindo"
    mensagem = "Obrigado por se cadastrar"
   