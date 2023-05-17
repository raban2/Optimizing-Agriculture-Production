# importing libraries
import pickle

from flask import Flask, request, jsonify

# unpickling the model
model = pickle.load(open('model.pkl', 'rb'))

# creating the object of the flask
app = Flask(__name__)


# creating the routes
@app.route('/')
def home():
    return "Hello World"


@app.route('/predict', methods=['POST'])
def predict():
    nitrogen = request.form.get('N')
    phosphorus = request.form.get('P')
    potassium = request.form.get('K')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')
    ph = request.form.get('ph')
    rainfall = request.form.get('rainfall')

    result = {'nitrogen': nitrogen, 'phosphorus': phosphorus, 'potassium': potassium, 'temperature': temperature,
              'humidity': humidity, 'ph': ph, 'rainfall': rainfall}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
