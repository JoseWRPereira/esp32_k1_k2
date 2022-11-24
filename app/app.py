from flask import Flask
from flask import jsonify, json
from flask import render_template, redirect, url_for, request
from flask import session
import requests
import urllib


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
    url = "http://api.thingspeak.com/channels/1952302/feeds.json?results=1"
    response = requests.get(url)
    ts = json.loads(response.content)
    print(ts)
    saida.set_k1( ts["feeds"][0]["field1"] )
    saida.set_k2( ts["feeds"][0]["field2"] )
    return jsonify([{"k1":saida.get_k1(), "k2":saida.get_k2()}])


@app.route("/thingspeak")
def ts():
    url = "https://api.thingspeak.com/update?api_key=87H93K3AI6OBGMZI&field1={}&field2={}".format(1,0)
    with urllib.request.urlopen(url) as response:
        print( response )
    return redirect(url_for('index'))



@app.route("/")
@app.route("/index")
def index():
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

    url = "https://api.thingspeak.com/update?api_key=87H93K3AI6OBGMZI&field1={}&field2={}".format(saida.get_k1(),saida.get_k2())
    with urllib.request.urlopen(url) as response:
        print( response )

    print("K1 = {};  K2 = {};".format(saida.get_k1(),saida.get_k2()) )

    return redirect(url_for('index'))
