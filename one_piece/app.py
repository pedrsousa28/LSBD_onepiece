from flask import Flask, render_template, redirect, request, url_for, flash
from flask_mysqldb import MySQL 

app = Flask (__name__)

app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="onepiece"
app.config["MYSQL_HOST"]="localhost"

mysql = MySQL(app) 


@app.route('/', methods=['POST', 'GET'])
def Index():
    if request.method == 'GET':
      Cursor = mysql.connection.Cursor()
      Cursor.execute("SELECT * FROM personagens")
      Data=Cursor.fetchall()
      Cursor.close()
    return render_template('index.html', perso=Data)



@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
      Nome = request.form['nome']
      Idade = request.form['idade']
      Lugar = request.form['lugar']
      Descricao = request.form['descricao']
      Cursor = mysql.connection.Cursor()
      Cursor.execute("INSERT INTO personagens (nome, idade, lugar, descricao) VALUES (%s, %s, %s, %s)", (Nome, Idade, Lugar, Descricao))
      mysql.connection.commit()
    return render_template('create.html', )
    

@app.route('/edit/<int:id>', methods=['POST','GET'])
def edit(id):
   if request.method == 'POST': 
     Nome = request.form['nome']
     Idade = request.form['idade']
     Lugar = request.form['lugar']
     Descricao = request.form['descricao']
     Cursor = mysql.connection.Cursor()
     Cursor.execute("UPDATE personagens SET nome=%s, idade=%s, lugar=%s, descricao=%s WHERE id=%s", (Nome, Idade, Lugar, Descricao, id))
     mysql.connection.commit()
   return render_template('edit.html')

@app.route('/<nome>', methods=['POST', 'GET'])
def personagens(nome):
   if request.method == 'GET':
     Cursor = mysql.connection.Cursor()
     Cursor.execute("SELECT * FROM personagens WHERE nome=%s", (nome))
     Data=Cursor.fetchall()
     Cursor.close()
   return render_template('persona.html', perso=Data)
   
   
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
   Cursor = mysql.connection.Cursor()
   Cursor.execute("DELETE FROM personagens WHERE id=%s", (id))
   mysql.connection.commit()
   return redirect (url_for('Index'))



if __name__ == "__main__":
  app.run(debug=True, port=5001)