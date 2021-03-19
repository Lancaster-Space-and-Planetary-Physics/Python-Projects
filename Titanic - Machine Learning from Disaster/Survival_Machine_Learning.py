import sys, os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

os.chdir('C:\\Users\\wiggsj\\Documents\\Practice Codes\\Python-Projects\\Titanic - Machine Learning from Disaster')

train_data = pd.read_csv('data\\train.csv')
test_data =  pd.read_csv('data\\test.csv')

y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('my_submission.csv', index=False)
print("Your submission was successfully saved!")
