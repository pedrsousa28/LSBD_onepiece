from flask import Flask, render_template, redirect, request, url_for, flash
from flask_mysqldb import MySQL 
from flask import request
from jinja2 import Environment, PackageLoader
env = Environment (loader=PackageLoader('app', 'templates'))

app = Flask (__name__)

app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="onepiece"
app.config["MYSQL_HOST"]="localhost"

mysql = MySQL(app) 


@app.route('/')
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM personagens")
    data=cursor.fetchall()
    cursor.close()
    return render_template('index.html')



@app.route('/', methods=['POST'])
def create():
    if request.method == 'POST':
      id = request.form['ID']
      nome = request.form['name']
      idade = request.form['idade']
      lugar = request.form['lugar']
      descricao = request.form['descricao']
      cursor = mysql.connection.connect()
      cursor.execute("INSERT INTO personagens (nome, idade, lugar, descricao) VALUES (%s, %s, %s, %s)", (nome, idade, lugar, descricao))
      mysql.connection.commit()
      return redirect(create.html)
    return ""

@app.route('/edit', methods=['GET', 'POST'])
def edit():
   if request.method == 'POST': 
     id = request.form['ID']
     nome = request.form['name']
     idade = request.form['idade']
     lugar = request.form['lugar']
     descricao = request.form['descricao']
     cursor = mysql.connection.cursor()
     cursor.execute("UPDATE personagens SET nome=%s, idade=%s, lugar=%s, descricao=%s", (nome, idade, lugar, descricao,))
     mysql.connection.commit()
     return ('edit.html')
   return ""
   
@app.route('/delete/<string:id>', methods=['GET'])
def delete(id):
   flash("")
   cursor = mysql.connection.cursor()
   cursor.execute("DELETE FROM personagens WHERE id=%s", (id,))
   mysql.connection.commit()
   return redirect (url_for('Index'))



if __name__ == "__main__":
  app.run(debug=True, port=5001)