from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

# Save the model to a file using pickle
log_reg = LogisticRegression()
with open('log_reg.pkl', 'wb') as f:
    pickle.dump(log_reg, f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/output', methods=['POST'])
def output():
    # Extract the input data from the form
    url_length = float(request.form['url_length'])
    total_of_at = float(request.form['total_of@'])
    total_of_www = float(request.form['total_of_www'])
    total_of_dash = float(request.form['total_of-'])
    total_of_percent = float(request.form['total_of%'])
    total_of_slash = float(request.form['total_of/'])
    
    # Dummy prediction
    prediction = 1
    
    # Map prediction to human-readable label
    if prediction == 1:
        predicted_label = "Phishing"
    else:
        predicted_label = "Legitimate"
    
    return render_template('output.html', prediction=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)
