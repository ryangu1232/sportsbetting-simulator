import pandas as pd
import numpy as np

table = {
    "count": ["abc", "def", "ghi"],
    "Age": ["kj", "sdf", "asd"]
}

df = pd.DataFrame(table)
print(df)

# Ensure the path below is correct or comment it out if not needed
# df = pd.read_csv('path_to_file.csv')
