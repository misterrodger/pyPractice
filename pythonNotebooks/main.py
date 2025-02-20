import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, np.nan, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

df.dropna(inplace=True)
print(df)
