from flask import Flask
from flask import jsonify, json
from flask import render_template, redirect, url_for, request

app = Flask(__name__)


class Saida():
    def __init__(self):
        self.k1 = 0
        self.k2 = 0


saida = Saida()

@app.route("/get")
def get():
    return jsonify([{"k1":saida.k1, "k2":saida.k2}])

@app.route("/")
def index():
    print("K1 = {};  K2 = {};".format(saida.k1,saida.k2) )
    return render_template("index.html", k_1=saida.k1, k_2=saida.k2)


@app.route("/saidas")
def saidas():
    t1 = request.args.get('K1')
    t2 = request.args.get('K2')

    if t1==None: 
        saida.k1 = 0
    else:
        saida.k1 = 1

    if t2==None:
        saida.k2 = 0
    else:
        saida.k2 = 1

    print("K1 = {};  K2 = {};".format(saida.k1,saida.k2) )
    return redirect(url_for('index'))



# if __name__=="__main__":
#     app.run()
