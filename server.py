'''
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv

. venv/bin/activate

pip install Flask

export FLASK_APP=server.py
export FLASK_ENV=development

flask run

pip install xgboost==0.90

heroku logs --tail
'''
#Loading the model
# run block of code and catch warnings
import xgboost as xgb
import pickle
model = pickle.load(open('./mode.pkl','rb'))



from flask import Flask, render_template, url_for , request,redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)
	

@app.route('/submit_form', methods = ['POST','GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		print(data)
		var = [float(data['amount_requested']),float(data['risk_score']),float(data['debt_to_income_ratio']),float(data['employment_length'])]
		# var = [7000.0, 732.0, 13.06, 10.0]
		# print(var)
		ans = int(model.predict(var)[0])
		# print(type(ans),ans)
		res = ["The Person is !NOT! Fit For Leanding Loan","The Person is Fit For Leanding Loan"]
		# var1 = "The Person is Fit For Leanding Loan"
		# var2 = "The Person is !NOT! Fit For Leanding Loan"
		return render_template("index.html",ansvar=res[ans])
		
	else:
		return 'Something went Wrong Try again'


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
