from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'onepiece' 
app.config['MYSQL_USER'] = "LUFFY"

mysql = MySQL(app)


@app.route('/')
def Index():   
    cur = mysql.connection.cursor()
    cur.execute ("SELECT * FROM personagens")
    data=cur.fetchall()
    cur.close()




    return render_template('index2.html', personagens=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("PERSONAGEM INSERIDO COM SUCESSO")
        nome = request.form['nome']
        idade = request.form['idade']
        lugar = request.form['lugar_de_origem']
        descricao = request.form['descricao']
        cursor= mysql.connection.cursor()
        cursor.execute("INSERT INTO personagens (nome, idade, lugar_de_origem, descricao) VALUES (%s, %s, %s, %s)", (nome, idade, lugar, descricao))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:nome>', methods = ['GET'])
def delete(nome):
    flash("Record Has Been Deleted Successfully")
    cursor=mysql.connection.cursor()
    cursor.execute("DELETE FROM personagens WHERE nome=%s", (nome,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        lugar = request.form['lugar_de_origem']
        descricao = request.form['descricao']
        cursor = mysql.connection.cursor()
        cursor.execute("""
               UPDATE personagens
               SET nome=%s, idade=%s, lugar_de_origem=%s, descricao=%s
               WHERE id=%s
            """, (nome, idade, lugar, descricao))
        flash("Atualizado")
        mysql.connection.commit()
        return redirect(url_for('Index'))









if __name__ == "__main__":
    app.run(debug=True)
