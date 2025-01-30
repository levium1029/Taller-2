import numpy as np

mu = 3
sigma = 1
n = 1000

vals = np.random.normal(mu, sigma, n)
print(vals)

import pandas as pd

df = pd.DataFrame(vals)
print(df.describe())