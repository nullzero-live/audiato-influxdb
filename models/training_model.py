'''Model Selection to come when data is available.

- Train model on maximum days of data (TBC)
- Either time series prediction of usage or anomaly detection
- Logisitic Regression is a place holder for now

- export for use with API endpoint hosted on FastAPI

'''

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression #Not to use
from sklearn.externals import joblib

#For training on 3 months of data
import pandas as pd
#Model tracking and evaluation
import wandb 

if wandb_api_key is not None:
    # Retrieve the value of wandb api key
    wandb.init(project="influx-db-audiato")
    wandb.login(key=wandb_api_key)
    
else:
    print("WANDB KEY NOT FOUND")
    

models = []

# Features and target
X = "DATAFRAME FEATURE"
y = "DATAFRAME TARGET"

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=42)

reg_model = LogisticRegression()
reg_model.fit(X_train, y_train)

# Log metrics at end of each model choice (How to use with pipelines in SKLearn)
wandb.log({"accuracy": accuracy})

#Serialize model
joblib.dump(reg_model, 'influx-model.pkl')