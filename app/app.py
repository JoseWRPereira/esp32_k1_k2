from flask import Flask
from flask import jsonify
from flask import render_template, redirect, url_for, request
from flask import session

app = Flask(__name__)
app.secret_key = 'k1k2'


class Saidas():
    def __init__(self):
        self.k1 = 0
        self.k2 = 0
    def get_k1(self):
        return self.k1
    def get_k2(self):
        return self.k2
    def set_k1(self, valor):
        self.k1 = valor
    def set_k2(self, valor):
        self.k2 = valor

saida = Saidas()

@app.route("/get")
def get():
    return jsonify([{"k1":saida.get_k1(), "k2":saida.get_k2()}])





@app.route("/")
@app.route("/index")
def index():
    saida.set_k1(session['k1'])
    saida.set_k2(session['k2'])
    print("K1 = {};  K2 = {};".format(saida.get_k1(),saida.get_k2()) )
    return render_template("index.html", k_1=saida.get_k1(), k_2=saida.get_k2())


@app.route("/saidas")
def saidas():
    t1 = request.args.get('K1')
    t2 = request.args.get('K2')
           

    if t1==None: 
        saida.set_k1(0)
    else:
        saida.set_k1(1)

    if t2==None:
        saida.set_k2(0)
    else:
        saida.set_k2(1)

    session['k1'] = saida.get_k1()
    session['k2'] = saida.get_k2()

    print("K1 = {};  K2 = {};".format(saida.get_k1(),saida.get_k2()) )
    return redirect(url_for('index'))
