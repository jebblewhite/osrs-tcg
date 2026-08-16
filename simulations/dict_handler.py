#python

import pandas as pd

df = pd.read_json('src/main/resources/Card.json')

print(df.columns)