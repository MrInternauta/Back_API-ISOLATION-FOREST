# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import json


def calculateAnomaly():
    df = pd.read_csv('salary.csv')
    model = IsolationForest(
        n_estimators=1, max_samples='auto', contamination=float(0.5), max_features=1.0)
    model.fit(df[['amount']])
    df['scores'] = model.decision_function(df[['amount']])
    df['anomaly'] = model.predict(df[['amount']])
    anomaly = df.loc[df['anomaly'] == -1]
    anomaly_index = list(anomaly.index)
    #print(anomaly)
    print(anomaly)
    outliers_counter = len(df[df['amount'] > 100]) + len(df[df['amount'] < 40])
    # print(outliers_counter)

    print("Accuracy percentage:", 100*list(df['anomaly']).count(-1)/(outliers_counter))

    data = json.dumps(anomaly.to_dict())
    response = {
        "status": True,
        "data":  (data)
    }
    return response
