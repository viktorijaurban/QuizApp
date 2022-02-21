from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

#Parbaudes lapa
@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(debug="true ")