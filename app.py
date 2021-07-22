from flask import Flask,render_template,request,send_file
from datetime import datetime

app = Flask(__name__) 

@app.route('/maps/GuddeBettaTruckingPlace')
def GuddeBettaTruckingPlace():
    return render_template('home.html')

@app.route('/')
def index():
    return render_template('index.html')
     
if __name__ == '__main__':

    app.run()