import joblib

def loading_model():
    print("Loading model....")
    
    with open("../models/model.pkl", 'rb') as f:
        svc_model = joblib.load(f) 
    
    print("Model Loaded")

    return svc_model
