'''Model Selection to come when data is available.

- Train model on 30 days of data (appears to be maximum)
- Either time series prediction of usage or anomaly detection
- Logisitic Regression is a place holder for now

- export for use with API endpoint hosted on FastAPI

'''

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression #Not to use
from sklearn.externals import joblib

#For training on 3 months of data
import pandas as pd 

# Features and target
X = "DATAFRAME FEATURE"
y = "DATAFRAME TARGET"

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=42)

reg_model = LogisticRegression()
reg_model.fit(X_train, y_train)

#Serialize model
joblib.dump(reg_model, 'influx-model.pkl')