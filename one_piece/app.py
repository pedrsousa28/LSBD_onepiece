from flask import Flask, render_template, redirect, request, url_for, flash
from flask_mysqldb import MySQL 
import os

app = Flask (__name__)

app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="onepiece"
app.config["MYSQL_HOST"]="localhost"

mysql = MySQL(app) 


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
      cursor = mysql.connection.cursor()
      cursor.execute("SELECT * FROM personagens")
      data=cursor.fetchall()
      cursor.close()
    return render_template('index.html', perso=data)



@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
      nome = request.form['nome']
      idade = request.form['idade']
      lugar = request.form['lugar']
      descricao = request.form['descricao']
      perfil = request.files['perfil']
      cursor = mysql.connection.cursor()
      cursor.execute("INSERT INTO personagens (nome, idade, lugar, descricao, fotoPersonagem) VALUES (%s, %s, %s, %s, %s)", (nome, idade, lugar, descricao, perfil))
      mysql.connection.commit()
      return redirect(url_for('index'))
    return render_template('create.html',)
    

@app.route('/edit/<int:id>', methods=['POST','GET'])
def edit(id):
   if request.method == 'POST':
     nome = request.form['nome']
     idade = request.form['idade']
     lugar = request.form['lugar']
     descricao = request.form['descricao']
     perfil = request.files['perfil']
     cursor = mysql.connection.cursor()
     cursor.execute("UPDATE personagens SET nome=%s, idade=%s, lugar=%s, descricao=%s fotoPersonagem=%s WHERE id=%s", (nome, idade, lugar, descricao, perfil, id))
     mysql.connection.commit()
     return redirect (url_for('index'))
   else:  # elif request.method == 'GET'   
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM personagens WHERE id=%s", (id,))
    data=cursor.fetchall()
    cursor.close() 
    print(data)
    return render_template('edit.html', perso=data[0])

@app.route('/<nome>', methods=['POST', 'GET'])
def personagens(nome):
   if request.method == 'GET':
     cursor = mysql.connection.cursor()
     cursor.execute("SELECT * FROM personagens WHERE nome=%s", (nome,))
     data=cursor.fetchall()
     cursor.close()
   return render_template('persona.html', perso=data)
   
   
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
   cursor = mysql.connection.cursor()
   cursor.execute("DELETE FROM personagens WHERE id=%s", (id,))
   mysql.connection.commit()
   return redirect (url_for('index'))



if __name__ == "__main__":
  app.run(debug=True, port=5001)