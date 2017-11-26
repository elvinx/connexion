#!/usr/bin/env python3

import connexion

from sklearn.externals import joblib

classifier = joblib.load('./classifier/model.pkl')


def post_predictions(query):
    predictions = []
    for item in query:
        text = item['text']
        category = classifier.predict([text])[0]
        predictions.append({"category": category, "text": text})
    return predictions


app = connexion.App(__name__)
app.add_api('swagger.yaml')

if __name__ == '__main__':
    app.run(port=8080, server='gevent')
