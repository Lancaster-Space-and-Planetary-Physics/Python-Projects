import sys, os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

os.chdir('C:\\Users\\wiggsj\\Documents\\Practice Codes\\Python-Projects\\Titanic - Machine Learning from Disaster')

train_data = pd.read_csv('data\\train.csv')
test_data =  pd.read_csv('data\\test.csv')

y = train_data["Survived"]

avg_male_age = (train_data.loc[train_data.loc[(train_data["Sex"]=="male") & (train_data["Age"].notnull())].index.to_numpy()]["Age"].sum())/len(train_data.loc[train_data.loc[(train_data["Sex"]=="male") & (train_data["Age"].notnull())].index.to_numpy()])
avg_female_age = (train_data.loc[train_data.loc[(train_data["Sex"]=="female") & (train_data["Age"].notnull())].index.to_numpy()]["Age"].sum())/len(train_data.loc[train_data.loc[(train_data["Sex"]=="female") & (train_data["Age"].notnull())].index.to_numpy()])
train_data.loc[(train_data["Sex"]=="male") & (train_data["Age"].isnull()),"Age"] = avg_male_age
train_data.loc[(train_data["Sex"]=="female") & (train_data["Age"].isnull()),"Age"] = avg_female_age

avg_male_age_test = (test_data.loc[test_data.loc[(test_data["Sex"]=="male") & (test_data["Age"].notnull())].index.to_numpy()]["Age"].sum())/len(test_data.loc[test_data.loc[(test_data["Sex"]=="male") & (test_data["Age"].notnull())].index.to_numpy()])
avg_female_age_test = (test_data.loc[test_data.loc[(test_data["Sex"]=="female") & (test_data["Age"].notnull())].index.to_numpy()]["Age"].sum())/len(test_data.loc[test_data.loc[(test_data["Sex"]=="female") & (test_data["Age"].notnull())].index.to_numpy()])
test_data.loc[(test_data["Sex"]=="male") & (test_data["Age"].isnull()),"Age"] = avg_male_age_test
test_data.loc[(test_data["Sex"]=="female") & (test_data["Age"].isnull()),"Age"] = avg_female_age_test

avg_3rd_fare_test =  (test_data.loc[test_data.loc[(test_data["Pclass"]==3) & (test_data["Fare"].notnull())].index.to_numpy()]["Fare"].sum())/len(test_data.loc[test_data.loc[(test_data["Pclass"]==3) & (test_data["Fare"].notnull())].index.to_numpy()])
test_data.loc[(test_data["Pclass"]==3) & (test_data["Fare"].isnull()),"Fare"] = avg_3rd_fare_test

features = ["Pclass", "Sex", "Age" ,"SibSp", "Parch", "Fare"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(5, 100, num = 20)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]


random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

model = RandomForestClassifier(n_estimators=500, max_depth=5, random_state=42, min_samples_split=5, min_samples_leaf= 1, max_features='sqrt',bootstrap=True)

#rf_random = RandomizedSearchCV(estimator = model, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)

# Fit the random search model
#rf_random.fit(X,y)

#print(rf_random.best_params_)

model.fit(X, y)
predictions = model.predict(X_test)

print(model.score(X,y))


#output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
#output.to_csv('my_submission.csv', index=False)
#print("Your submission was successfully saved!")
