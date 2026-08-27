import numpy as np
import pandas as pd


numbers = np.array([10, 20, 30, 40, 50])
table = pd.DataFrame({"number": numbers})

print("Python learning environment is ready!")
print(table)
print(f"Average: {table['number'].mean()}")