import pickle
import pandas as pd
import numpy as np
import os
from django.conf import settings

class FraudDetectionModel:
    def __init__(self, model_path=None):
        if model_path is None:
            model_path = settings.ML_MODEL_PATH
        
        # Load the model
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)
        
        # Feature names expected by the model
        self.feature_columns = [
            'Sent tnx', 'Received Tnx', 'Avg min between sent tnx',
            'Avg min between received tnx', 'Time Diff between first and last (Mins)',
            'ERC20 uniq sent token name', 'ERC20 uniq rec token name',
            'Number of Created Contracts'
        ]
    
    def preprocess_data(self, wallet_address, blockchain_data):
        """
        Preprocess wallet data to extract the features expected by the model.
        """
        features = {
            'Sent tnx': blockchain_data.get('Sent tnx', 0),
            'Received Tnx': blockchain_data.get('Received Tnx', 0),
            'Avg min between sent tnx': blockchain_data.get('Avg min between sent tnx', 0),
            'Avg min between received tnx': blockchain_data.get('Avg min between received tnx', 0),
            'Time Diff between first and last (Mins)': blockchain_data.get('Time Diff between first and last (Mins)', 0),
            'ERC20 uniq sent token name': blockchain_data.get('ERC20 uniq sent token name', 0),
            'ERC20 uniq rec token name': blockchain_data.get('ERC20 uniq rec token name', 0),
            'Number of Created Contracts': blockchain_data.get('Number of Created Contracts', 0)
        }
        
        # Convert to DataFrame and ensure correct order of features
        df = pd.DataFrame([features])[self.feature_columns]
        return df
    
    def predict(self, wallet_address, blockchain_data):
        """
        Predict if a wallet is fraudulent based on blockchain data.
        """
        features_df = self.preprocess_data(wallet_address, blockchain_data)
        confidence = self.model.predict_proba(features_df)[0, 1]
        is_fraudulent = confidence > 0.7  
        
        return is_fraudulent, confidence

# Singleton pattern to avoid loading the model multiple times
_model_instance = None

def get_model():
    global _model_instance
    if _model_instance is None:
        _model_instance = FraudDetectionModel()
    return _model_instance
