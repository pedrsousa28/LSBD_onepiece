from flask import Flask, render_template, redirect, request, url_for, flash
from flask_mysqldb import MySQL

app = Flask (__name__)

app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="onepiece"
app.config["MYSQL_HOST"]="localhost"

mysql = MySQL(app)

@app.route('/')
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM perso")
    data=cursor.fetchall()
    cursor.close()
    return render_template ( 'index.html', perso=data )



@app.route('/create', methods = ['POST'])
def create():
    if request.method == "POST":
     nome=request.form['nome']
     idade = request.form['idade']
     lugar = request.form['lugar']
     descricao = request.form['descricao']
     cursor = mysql.connector.connect()
     cursor.execute("INSERT INTO perso (nome, idade, lugar, descricao) VALUES (%s, %s, %s, %s)", (nome, idade, lugar, descricao))
     mysql.connector.commit()
     return redirect(url_for('Index'))

@app.route('/edit', methods=['POST,GET'])
def edit():
   if request.method == "POST":
     nome=request.form['nome']
     idade = request.form['idade']
     lugar = request.form['lugar']
     descricao = request.form['descricao']
     cursor = mysql.connector.connect()
     cursor.execute("UPDATE perso SET nome=%s, idade=%s, lugar=%s, descricao=%s", (nome, idade, lugar, descricao,))
     mysql.connector.commit()
     return redirect (url_for('Index'))
   





   if __name__ == "__main__":
    app.run(debug=True)