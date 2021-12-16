from flask import Flask, make_response, request, jsonify
from sklearn.pipeline import Pipeline
from lightgbm import LGBMClassifier
import pandas as pd
import joblib
import numpy

app = Flask(__name__)

lgbmc_model = joblib.load('models/lgbmc.pkl')

args_name = ['age', 'sex', 'chestPainType', 'restingBP', 'cholesterol',
             'fastingBS', 'restingECG', 'maxHR', 'exerciseAngina', 'oldpeak', 'sTSlope']
args_col = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol',
               'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']
args_type = [int, str, str, int, int, int, str, int, str, float, str]


@app.route('/predict-heart-disease', methods=['POST'])
def predict_heart_disease():
    # Format validation
    if (not request.is_json):
        return make_response({'message': 'Only JSON format is accepted'}, 400)

    # Variable and data type validation
    content = request.get_json()
    args_value = []
    for i in range(len(args_name)):
        arg_name = args_name[i]
        arg_type = args_type[i]
        if arg_name not in content.keys():
            return make_response({'message': 'The variable ' + arg_name + ' is missing'}, 400)
        else:
            if type(content[arg_name]) is not arg_type:
                return make_response({'message': 'The variable is not of the correct type'}, 400)
            else:
                args_value.append(content[arg_name])

    # Probability prediction
    x = pd.DataFrame(numpy.array([args_value]), columns=args_col)
    prob = lgbmc_model.predict_proba(x)

    response = jsonify({'prob': float(prob[0][1])})
    return make_response(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
