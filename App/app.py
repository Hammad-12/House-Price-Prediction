from flask import Flask, render_template, request
import joblib
import numpy as np

model = joblib.load('D:\PROJECTS\REGRESSION\model\model_joblib')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_price():
    total_sqft = float(request.form.get('total_sqft'))
    bath = int(request.form.get('bath'))
    balcony = int(request.form.get('balcony'))
    area_type = request.form.get('area_type')
    if area_type == 'sa':
        ba = 0
        ca = 0
        pa = 0
        sa = 1
    elif area_type == 'ba':
        ba = 1
        ca = 0
        pa = 0
        sa = 0
    elif area_type == 'ca':
        ba = 0
        ca = 1
        pa = 0
        sa = 0
    else:
        ba = 0
        ca = 0
        pa = 1
        sa = 0

    bhk = int(request.form.get('bhk'))

    # prediction
    result = model.predict(np.array([total_sqft, bath, balcony,ba, ca, pa, sa, bhk]).reshape(1,8))

    return render_template('index.html',result=result[0] * 100000)


if __name__ == '__main__':
    app.run(debug=True)
