from flask import Flask, render_template, request
import pickle
import numpy as np

filename = 'prognosis.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/prognosis', methods=['POST'])
def predict():
	a = 1
	c = int(request.form['crop'])
	n = float(request.form['nitrogen%'])
	npa = float(request.form['nitrogen_pa'])
	p = float(request.form['pottasium%'])
	ppa = float(request.form['pottasium_pa'])
	po = float(request.form['potash%'])
	popa = float(request.form['potash_pa'])
	r = float(request.form['rain'])
	t = float(request.form['temp'])
	data = np.array([[a,c,n,npa,p,ppa,po,popa,r,t]])
	p = model.predict(data)
	return render_template('result.html', result=p)
	

if __name__ == '__main__':
	app.run(debug=True)
