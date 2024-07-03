
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from catboost import CatBoostRegressor, Pool
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), 'model.joblib')
try:
    model = joblib.load(model_path)
    if not hasattr(model, 'predict'):
        raise ValueError(f"The loaded object is not a valid model: {model}")
except FileNotFoundError:
    raise FileNotFoundError(f"Model file not found at {model_path}")

def predictor(data):

    feature4 = data['long']
    feature3 = data['lat']
    feature2 = data['depth']


    input_features = np.array([[feature2,feature3,feature4]])

    y_pred = model.predict(input_features)
    print(f'Y:{y_pred}')
    return y_pred[0]