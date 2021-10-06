
from flask import Flask, render_template, request, session
import joblib

app = Flask(__name__)
pipeline = joblib.load('./StockPrice.pkl')

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/prediction')
def predi():
    return render_template('prediction.html')

@app.route('/predict1',methods =['POST','GET'])
def pred():
    s = []
    if request.method== 'POST':
        date= request.form['date']
        Previous_CP = request.form['pcp']
        OpenPrice = request.form['op']
        HighPrice = request.form['hp']
        LowPrice = request.form['lp']
        LastPrice = request.form['lap']
        ClosePrice = request.form['cp']
        s.extend([date,Previous_CP,OpenPrice,HighPrice,LowPrice,LastPrice,ClosePrice])
        pred = pipeline.predict([s])
        return render_template('prediction.html', msg="success", op=pred)


if __name__ =='__main__':
     app.run(debug=True)