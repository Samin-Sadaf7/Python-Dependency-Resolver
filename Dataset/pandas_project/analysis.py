import numpy as np
import pandas as pd

data = pd.DataFrame({'values': np.random.rand(10)})
print(data.describe())