import numpy as np
from flask import Flask, request, render_template, redirect, url_for
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model_rfc.pkl", "rb"))
scalar = pickle.load(open("scaling.pickle", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    pre_final_features = [np.array(int_features)]
    final_features = scalar.transform(pre_final_features)
    prediction = model.predict(final_features)

    if prediction[0] == 2:
        output = "Good"
    elif prediction[0] == 1:
        output = "Standard"
    else:
        output = "Poor"

    # Redirect to the result page with the prediction
    return redirect(url_for('result', prediction_text=output))

@app.route('/result')
def result():
    prediction_text = request.args.get('prediction_text', '')
    return render_template('result.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
