
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(filepath='customer_data.csv'):
    # Load data
    data = pd.read_csv(filepath)
    
    # Preprocess data (e.g., dropping missing values, scaling features)
    data.dropna(inplace=True)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[["Annual_Income", "Spending_Score"]])  # Example column names
    
    return scaled_data
