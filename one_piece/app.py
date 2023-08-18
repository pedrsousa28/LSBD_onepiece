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
    cursor.execute("SELECT * FROM personagens")
    data=cursor.fetchall()
    cursor.close()
    return render_template('index.html')



@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
      nome = request.form['name']
      idade = request.form['idade']
      lugar = request.form['lugar']
      descricao = request.form['descricao']
      cursor = mysql.connection.cursor()
      cursor.execute("INSERT INTO personagens (id, nome, idade, lugar, descricao) VALUES (%s, %s, %s, %s, %s)", (id, nome, idade, lugar, descricao))
      mysql.connection.commit()
      return redirect(url_for('create'))
    return ""

@app.route('/edit', methods=['GET', 'POST'])
def edit():
   if request.method == 'POST': 
     nome = request.form['name']
     idade = request.form['idade']
     lugar = request.form['lugar']
     descricao = request.form['descricao']
     cursor = mysql.connection.cursor()
     cursor.execute("UPDATE personagens SET id=%s, nome=%s, idade=%s, lugar=%s, descricao=%s", (id, nome, idade, lugar, descricao,))
     mysql.connection.commit()
     return redirect(url_for('edit'))
   return ""
   
@app.route('/delete/<string:id>', methods=['GET'])
def delete(id):
   flash("Foi Apagado")
   cursor = mysql.connection.cursor()
   cursor.execute("DELETE FROM personagens WHERE id=%s", (id,))
   mysql.connection.commit()
   return redirect (url_for('Index'))



if __name__ == "__main__":
  app.run(debug=True, port=5001)