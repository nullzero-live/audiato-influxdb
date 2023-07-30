'''
1. TRAIN MODEL
2. EVAL MODEL
3. WANDB LOGIN

Model Selection to come when data is available.

- Train model on maximum days of data (TBC)
- Either time series prediction of usage or anomaly detection
- Logisitic Regression is a place holder for now

- export for use with API endpoint hosted on FastAPI

'''
import os

from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from datetime import datetime

#For training on 3 months of data
import pandas as pd
#Model tracking and evaluation
import wandb 
from models import Model

def wandb_login():
    wandb_api_key = os.getenv("WANDB_API_KEY")

    if wandb_api_key is not None:
        # Retrieve the value of wandb api key
        try:
            wandb.init(project="influx-db-audiato", mode="disabled")
            wandb.login(key=wandb_api_key)
        except Exception as e:
            print("WANDB LOGIN ERROR: {}".format(e))
            
def load_data():
    wandb_login()
    
    file_path = "PATH TO FILE"
    with wandb.init(project="influx-db-audiato", job_type="load-data") as run:
        df = pd.read_csv(file_path)
        raw_data = wandb.Artifact('DATASET NAME', 
                                type= ".dataset",
                                description= "DATASET DESCRIPTION")
        run.log_artifact(raw_data)
    return df

    
def train_model(model):
    df = load_data()
    # Features and target
    X = df.drop["target"]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, 
                                                        random_state=42)
    
    #Models for use
    models = ['Logistic regression', 'Decision Trees', 'Random Forest', 'Voting Classifier', 'XGBoost']
    
    for model in models:
        train_model = Model(model).get_model()
        train_model.fit(X_train, y_train)
        
        # Log metrics at end of each model choice (How to use with pipelines in SKLearn)
        eval_model(model=model, X_test=X_test, y_test=y_test)
    
        #Serialize model
        joblib.dump(train_model, f'{model}_trained.pkl')
        

def eval_model(model, X_test, y_test):
    #Generate predictions
    y_pred = train_model.predict(X_test)
    y_probas = clf.predict_proba(X_test) # Use in WandBLogs
    
    #Accuracy Metrics
    accuracy = accuracy_score(y_test, y_pred)
    f1, auc, score = calculate_metrics(model, X_test ,y_test, y_pred)
    
    with open('results.txt', 'w') as f:
        f.write(f"\n### {datetime.now()} ###\n")
        f.write(f"Accuracy: {print(accuracy_score(X_test, y_test))}\n")
        f.write("F1 =", f1, "AUC score", auc, "Accuracy", score)
    
    #W&B Evaluations -- ADD MORE METRICS
    wandb.log({f"{model}_accuracy": accuracy})
    #https://colab.research.google.com/github/wandb/examples/blob/master/colabs/scikit/Simple_Scikit_Integration.ipynb
    
    