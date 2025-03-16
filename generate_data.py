import numpy as np
import pandas as pd

def generate_data(num_samples=1000):
    # Generate synthetic data
    np.random.seed(42)
    X = np.random.rand(num_samples, 10)
    y = (X.sum(axis=1) > 5).astype(int)
    
    # Create a DataFrame
    data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
    data['target'] = y
    
    # Save the data to CSV
    data.to_csv('synthetic_data.csv', index=False)
    print("Synthetic data generated and saved to synthetic_data.csv")

if __name__ == "__main__":
    generate_data()