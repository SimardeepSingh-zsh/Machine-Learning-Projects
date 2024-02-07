import pandas as pd
import numpy as np

# Number of samples
n_samples = 100

# Generate random data
data = np.random.rand(n_samples, 5)

# Create a DataFrame
df = pd.DataFrame(data, columns=['Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5'])

# Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False)
